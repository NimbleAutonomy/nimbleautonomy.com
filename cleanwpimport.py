import argparse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import os
import re

def get_downloads_from_img(img):
    return_list = []
    src = img.get('src')
    if src is not None:
        parsed = urlparse(src)
        filename = os.path.basename(parsed.path)
        return_list.append((filename, src, src))
    srcset = img.get('srcset')
    if srcset is not None:
        srcs = srcset.split(',')
        for src in srcs:
            original = src
            src = src.strip()
            src = src.split(' ')[0]
            parsed = urlparse(src)
            filename = os.path.basename(parsed.path)
            return_list.append((filename, src, original))

    return return_list


def find_url(possible_url):
    finds = re.findall('(?i)\\b((?:https?://|www\\d{0,3}[.]|[a-z0-9.\\-]+[.][a-z]{2,4}/)(?:[^\\s()<>]+|\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\))+(?:\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\)|[^\\s`!()\\[\\]{};:\'\\".,<>?«»“”‘’]))', possible_url)
    if len(finds) == 0:
        return None
    return finds[0][0]


def find_image_matches(url, file_paths):
    return [(filename, src, original) for filename, src, original in file_paths if src == url]


def update_image_tag(img, file_paths, soup):
    newimg = soup.new_tag('img')
    SKIP_ATTRS = ['class', 'style']
    for attr in img.attrs:
        if attr not in SKIP_ATTRS:
            if attr == 'src':
                matches = find_image_matches(img.attrs[attr], file_paths)
                newimg.attrs[attr] = 'images/' + matches[0][0]
            elif attr == 'srcset':
                new_srcset = img.attrs[attr]
                for path in file_paths:
                    orig_split = path[2].split(' ')
                    if len(orig_split) > 1:
                        new_srcset = new_srcset.replace(path[1], 'images/'+path[0])
                newimg.attrs[attr] = new_srcset
            else:
                newimg.attrs[attr] = img.attrs[attr]

    return newimg


parser = argparse.ArgumentParser(description='cleanup a file imported to markdown from wordpress.xml using pelican-import')
parser.add_argument('markdownfile', type=argparse.FileType('r'))
parser.add_argument('wordpressxmlfile', type=argparse.FileType('r'))
parser.add_argument('--outputdirectory', default='', type=str)
parser.add_argument('--imagesdirectory', default='', type=str)
args = parser.parse_args()

outputfile = os.path.join(args.outputdirectory, os.path.basename(args.markdownfile.name))
imagepath = os.path.join(args.outputdirectory, args.imagesdirectory)
if args.outputdirectory:
    os.makedirs(args.outputdirectory, exist_ok=True)
if args.imagesdirectory:
    os.makedirs(imagepath, exist_ok=True)

lines = []
with args.markdownfile as f:
    lines = f.readlines()

# get rid of the obvious stuff I don't want
newlines = []
extratags = []
for line in lines:
    if line.startswith('Category: '):
        category = line[10:]
        commaloc = category.find(',')
        if commaloc != -1:
            onecategory = category[:commaloc]
            print(f'WARNING: multiple categories found, selecting the first one: {onecategory}, and turing the rest to tags')
            newlines.append(f'Category: {onecategory}\n')
            extratags = category[commaloc:].split(',')
            continue

    if line.startswith('Tags: ') and len(extratags) > 0:
        print(line)
        line = line.rstrip()
        for tag in extratags:
            tag = tag.strip()
            if len(tag) > 0:
                line += ', ' + tag
        line += '\n'
        print(line)
        newlines.append(line)
        continue

    if not (line.startswith('Author: ') or \
            line.startswith('Status:') or \
            line.startswith('`<!-- wp:paragraph') or \
            line.startswith('`<!-- /wp:paragraph') or \
            line.startswith('--')):
        newlines.append(line)

# clean up ugly header gunk
newlines2 = []
inheading = False
title = ''
for line in newlines:
    if line.startswith('Title: '):
        # remove the metadata
        title = line[7:].rstrip()
    elif line.startswith('`<!-- wp:heading'):
        inheading = True
        continue
    elif line.startswith('`<!-- /wp:heading'):
        inheading = False
        continue
    elif inheading and len(line) == 1:
        continue
    if inheading:
        if not line.startswith('#'):
            newline = '# ' + line
        else:
            newline = line
        newlines2.append(newline)
        continue
    newlines2.append(line)

# clean up redundant blank lines
newlines3 = []
lastline = ''
for line in newlines2:
    if (line == lastline) and len(line) == 1:
        continue
    lastline = line
    newlines3.append(line)

# clean up poor spaces in lists
newlines4 = []
inlist = False
for line in newlines3:
    if line.startswith('`<!-- wp:list'):
        inlist = True
        continue
    elif line.startswith('`<!-- /wp:list'):
        inlist = False
        continue
    elif inlist and len(line) == 1:
        continue
    elif inlist and line.startswith('-  '):
        line = '- ' + line[4:]
    newlines4.append(line)

original_url = ''
linkline = ''
blogtitle = ''
# parse the wordpress xml to get original link
tree = ET.parse(args.wordpressxmlfile.name)
root = tree.getroot()
item = root.find('./channel/title')
if item is not None:
    blogtitle = item.text

for item in root.findall('./channel/item'):
    title_element = item.find('./title')
    if not ((title_element is not None) and title == title_element.text):
        continue
    
    link_element = item.find('./link')
    if link_element is not None:
        original_url = link_element.text

    if blogtitle:
        linkline = f'*Originally published on [{blogtitle}]({original_url})*\n'
    else:
        linkline = f'*Originally published at [{original_url}]({original_url})*\n'
    break;

newlines4.append('\n')
newlines4.append(linkline)

newlines5 = []
# get the images
if original_url:
    post_thumbnail_img = None
    images = []

    response = urllib.request.urlopen(original_url)
    original_post = response.read()
    soup = BeautifulSoup(original_post, features="lxml")
    
    article = soup.find('article')
    if article is not None:
        thumbnail_div = article.find('div', {'class': 'post-thumbnail'})
        if thumbnail_div is not None:
            post_thumbnail_img = thumbnail_div.find('img')
        else:
            thumbail_a = article.find('a', {'class': 'post-thumnbnail'})
            if thumbail_a is not None:
                post_thumbnail_img = thumbnail_a.find('img')
    
        entry_content_div = article.find('div', {'class': 'entry-content'})
        if entry_content_div is not None:
            images = entry_content_div.findAll('img')
    
    # make a list of images to download
    downloads = []
    if post_thumbnail_img is not None:
        downloads.extend(get_downloads_from_img(post_thumbnail_img))

    for image in images:
        downloads.extend(get_downloads_from_img(image))

    # download the images
    for download in downloads:
        print(f'downloading: {download[1]}')
        urllib.request.urlretrieve(download[1], os.path.join(imagepath, download[0]))

    if post_thumbnail_img is not None:
        # find the first non-metadata content line by finding the first line after an empty line
        line_num = 0
        for line in newlines4:
            if len(line) == 1:
                line_num += 1
                break
            line_num+=1

        new_thumbnail = update_image_tag(post_thumbnail_img, downloads, soup)
        newlines4.insert(line_num, str(new_thumbnail)+'\n')
        newlines4.insert(line_num+1, '\n')

    # clean up images
    inimg = False
    for line in newlines4:
        if line.startswith('`<!-- wp:image'):
            inimg = True
            continue
        elif line.startswith('`<!-- /wp:image'):
            inimg = False
            continue
        elif inimg and len(line) == 1:
            continue
        elif inimg and line.startswith('!['):
            imgurl = find_url(line)
            if imgurl is None:
                continue
            # find the original image tag
            for image in images:
                if image['src'] == imgurl:
                    new_image = update_image_tag(image, downloads, soup)
                    newlines5.append(str(new_image)+'\n')
                    break
        else:
            newlines5.append(line)

else:
    newlines5 = newlines4

with open(outputfile, 'w') as f:
    f.writelines(newlines5)

