import argparse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import os


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


parser = argparse.ArgumentParser(description='cleanup a file imported to markdown from wordpress.xml using pelican-import')
parser.add_argument('markdownfile', type=argparse.FileType('r'))
parser.add_argument('wordpressxmlfile', type=argparse.FileType('r'))
args = parser.parse_args()

lines = []

with args.markdownfile as f:
    lines = f.readlines()

# get rid of the obvious stuff I don't want
newlines = []
for line in lines:
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
    if line.startswith('`<!-- wp:heading'):
        inheading = True
        continue
    if line.startswith('`<!-- /wp:heading'):
        inheading = False
        continue
    if inheading and len(line) == 1:
        continue
    if inheading:
        newline = '# ' + line
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
    if line.startswith('`<!-- /wp:list'):
        inlist = False
        continue
    if inlist and len(line) == 1:
        continue
    if inlist and line.startswith('-  '):
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
    
        entry_content_div = article.find('div', {'class': 'entry-content'})
        if entry_content_div is not None:
            images = entry_content_div.findAll('img')
    
    # make a list of images to download
    downloads = []
    downloads.extend(get_downloads_from_img(post_thumbnail_img))

    for image in images:
        downloads.extend(get_downloads_from_img(post_thumbnail_img))

    for download in downloads:
        print(f'downloading: {download[1]}')
        urllib.request.urlretrieve(download[1], download[0])

with open('new.md', 'w') as f:
    f.writelines(newlines4)

