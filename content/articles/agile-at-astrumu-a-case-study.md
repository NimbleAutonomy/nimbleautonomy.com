Title: Agile at AstrumU: A Case Study
Date: 2019-02-04 08:00
Category: Agile
Tags: agile, JIRA, product development, AstrumU, Software Engineering
Slug: agile-at-astrumu-a-case-study

# Introduction

This article is meant to present how we organize our work at AstrumU, a startup based in the US in Seattle with remote offices for sales and some of the development team. Our development team has grown significantly over the last six months. The company is about a year old.

Our product is composed of multiple web-based front-end applications backed by a steadily increasing number of microservices.

# My Biases 

I'm going to state some of my biases up-front. I firmly ascribe to the dictum that you don't let your tools dictate your process. I am also a firm believer in using a physical board for a team to organize work.

In my experience, a physical board is only useful with a co-located team. I have managed distributed agile teams for many years. I have not found a way to avoid using a digital board when the team doesn't physically sit together.

I have used many of the agile digital tools over the years. I am not a strong advocate for any particular one. When I joined AstrumU, we were already using Jira, and I saw no reason to switch to a different tool. There are some workflows that we've built in Jira that might be useful for other teams, so I include them here.

Jira is such a catch-all tool that its' complexity makes it difficult for teams to adopt. I'm hoping that our workflows might show other teams some useful things that Jira can do.  

# Our Agile Process 

At AstrumU we use a simple Kanban process, with some of the ceremonies from Scrum. Some call this "Scrumban."

We have a daily standup at 9 am in the US. On Mondays, we follow the stand-up with a retrospective or a planning meeting (alternating weeks). The retrospectives and standup are similar to the traditional Scrum ceremonies so I won't describe them here. Our planning meeting is different. I describe it later in a later section.

# Projects and How We Use Them 

Given that we build multiple products and a variety of independent supporting services, it makes sense not to have one project for all of our development or one project per team to track work. Instead, we use multiple projects that are each specific to a product or supporting service. We currently have 14 different projects in Jira covering everything from an application front-end to our cross-service security work.

We try to keep the projects clear enough that it is obvious where a work-item should go, but it can still be sometimes confusing to identify the right project for a new task. We're working to make this more apparent.

A benefit of this structure is that we can leverage pull requests in our GitHub projects to transition stories to the "done" and "released" states automatically as the code moves from a feature branch to the develop branch to the main line.

To track the overall work of the team, we have a master AstrumU project that consolidates and tracks all the work in the other projects. The AstrumU project is the only one in Jira that has a Kanban view and is the single source of truth for prioritization and work-in-progress. This project is also where work items that span multiple projects, such as infrastructure or general documentation, are added.

<img alt="" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" src="/articles/images/AstrumU_Filter_Query-1.png" srcset="/articles/images/AstrumU_Filter_Query-1.png 886w, /articles/images/AstrumU_Filter_Query-1-420x361.png 420w, /articles/images/AstrumU_Filter_Query-1-744x640.png 744w, /articles/images/AstrumU_Filter_Query-1-768x661.png 768w"/>

# Taxonomy of our work items 

We have four different packages of work: Epics, Stories, Tasks, and Bugs. We use the Jira built-in types for these. Each has a different use, scope, and meaning in our workflow.

### Epics 

The product team works with the development and data teams to create Jira Epics in the AstrumU project to capture substantial efforts such as an MVP of a new feature. Epics are sized to be a reasonable amount of work to complete within a few weeks or less of dedicated development time (i.e., "Students Can Register On the Site" not "Build the Student App MVP"). The Epic ticket includes as much context as possible: links to user research, UI designs, and product concept documents, for example. The Epic also includes acceptance criteria (a.k.a. the definition of done).  

### Stories 

The development and data teams break the Epics down into Stories to track the implementation and design work. We size Stories for completion within a day or two at most (i.e., "Route \<url\> to new service in Traefik" not "Create the Student API service"). The work for a story includes time to write tests and validate that the code works. The work also includes things like adding telemetry or monitoring as appropriate. The majority of Stories link to an Epic, but that is not a requirement. Stories without Epics tend to be one-off maintenance efforts, small incremental improvements to a feature or refactoring or other technical debt.

Stories should always contain acceptance and enough context that any developer who picks up the task has all the information needed to complete the work. The context is especially critical because of the distributed nature of the team. We have found problems when a story is missing this information because a developer cannot complete it without having to wait for standup to get the missing context. We have also had stories done incorrectly because of missing context.  

### Tasks 

If, as part of defining or working on a Story, we come across a small separable effort for someone else to take over and work on independently, we create a Task and link it to the Story.

Scoping for a Task is in the range of a few hours. If a Task is enough work to be a day or longer, it should be a Story instead. If the Task is simple one-off maintenance or a hygiene effort, we do not link it to a Story or Epic.  

### Bugs 

Bugs are indicators of something broken in existing code. Bugs are not used to specify new or incremental feature work. Refactoring code or reorganizing repositories is not bug work. A page rendering incorrectly or an API failing are examples of bugs.

We file Bugs against the most appropriate Jira project for the issue. We encourage anyone in the company to file a bug when they find it. For folks who don't know what Project to file the bug against, they file it against the AstrumU project, and it is moved to the appropriate project later.  

# Organizing and Tracking the Work 

We have two Kanban Boards in the AstrumU project. One tracks Epics only and the other tracks Stories, Tasks, and Bugs.  

### The Epic Kanban Board 

Since our epics track the significant efforts in progress, the Epic board is an evident view of the work that the teams are doing and what is next. For those who do not need to follow the details of the work, this is an excellent view-at-a glance of the state of the world. If you want more detail about an Epic, you can open the Epic to see what work is complete and what work remains.

Our Kanban board for Epics has three columns: To Do, In Progress, and Done. The simplicity of the columns makes sense for an Epic workflow where the primary goal is transparency and managing the amount of work in progress. We also maintain a backlog for Epics.

<img alt="" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" src="/articles/images/ASUEpics_Kanban-1200x730.png" srcset="/articles/images/ASUEpics_Kanban-1200x730.png 1200w, /articles/images/ASUEpics_Kanban-420x256.png 420w, /articles/images/ASUEpics_Kanban-744x453.png 744w, /articles/images/ASUEpics_Kanban-768x467.png 768w, /articles/images/ASUEpics_Kanban.png 1509w"/>

The ordering of Epics in the columns denotes priority, but there is no strict enforcement of having the stories in the other board match the epic prioritization exactly. If there is a significant disparity, that in itself would signal some potential issues in our process.

An Epic moves from the To Do to the In Progress column when it is ready for work by the whole team if there are people available to work on it. There may be some Stories that we start on in Epics that are still in the To Do column. That is almost always cards for the UX or Product Managers to prepare the Epic for the rest of the team.

Epics move from In Progress to Done when all the stories, tasks, and bugs attached to the Epic are complete, and the Product, UX, and Engineers sign off on the Acceptance Criteria (this is very informal).

Epics move from the Done column off of the board after the bi-weekly planning meeting (described later) if all code elements from the Epic are now running in Production.  

### The Detail Board 

<img alt="The detail Kanban board" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" src="/articles/images/Detail_Kanban-1200x729.png" srcset="/articles/images/Detail_Kanban-1200x729.png 1200w, /articles/images/Detail_Kanban-420x255.png 420w, /articles/images/Detail_Kanban-744x452.png 744w, /articles/images/Detail_Kanban-768x467.png 768w, /articles/images/Detail_Kanban.png 1512w"/>

The board that the development and UX teams most interact with is the Story/Task/Bug Kanban board. This board contains five columns: To Do, Blocked, In Progress, In Review and Done. Without context, this board can look very chaotic with all the stories from different teams, different projects and different epics. In reality, the team likes it because it shows very clearly what things are complete, what is in progress, and what is next.

Most of the time we have a single swim lane, but when we have any time-critical cards, we use a separate Expedite swim lane to track them.

The cards' position in the column denotes priority. Developers are expected to take their next work item from as near the top of the To Do column as they can. Because each card that is part of an Epic has the title and color of that Epic on the card, it is straightforward to see if the prioritization of the cards aligns with the priorities of the Epics.

Cards move from To Do to In Progress when a developer is free. We do not let a single developer have more than one card In Progress. When a developer starts work on a card, if they realize that the scope of the work is too big for a story, they break down the card into smaller stories and tasks. They can keep moving forward on their work. We discuss the breakdown in the next day's standup. If the team agrees on the new stories and tasks, those cards get prioritized in the To Do column.

<img alt="" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" src="/articles/images/Story-Workflow.png" srcset="/articles/images/Story-Workflow.png 975w, /articles/images/Story-Workflow-420x268.png 420w, /articles/images/Story-Workflow-744x474.png 744w, /articles/images/Story-Workflow-768x489.png 768w"/>

If a Developer is working on a card and finds that a dependency on another card is blocking their work, they link the two cards and then move the blocked card to the Blocked column. A card only moves to the Blocked column if the blocking dependency is In Progress. If the dependency is the To Do column, then the developer adds comments about what they have done, they push their in-progress branch to Github and then put the card back in To Do and start on something else.

Once the work for a card is done and tested locally, the developer submits a Pull Request for their feature branch and moves the card to the In Review column. Each code change requires two other developers to review and approve the change. When the Pull Request merges into the Development branch, the card moves from In Review to the Done column automatically.

When a release is created in GitHub as part of our semantic versioning scheme and the code moves from our Development cluster to our Production cluster, there is a parallel release done in Jira, and the stories move off of the Kanban board.

I have been considering doing a separate column for UX Review on the Kanban board and may add that in future.

### The Planning Meeting 

Every other week after the Monday standup meeting we have our planning meeting. The agenda of the meeting is: Review the completed Epics from the last two weeks; review the Epics that are currently in progress and review any new epics that may be moved from To Do to In Progress in the next two weeks.

For the In Progress Epics, we discuss the work remaining with an eye towards making sure the remaining stories satisfy the acceptance criteria of the Epic. If not, we may need to add additional stories.

For the upcoming Epics, we discuss the product, UX and business context of the Epic so that the teams understand why we are working on this Epic next and why it is relevant to our business. We make sure the acceptance criteria is understood. For feature work, the Product Manager and UX designer discuss the rationale behind the epic and the initial UX designs. The development team then reviews the cards associated with the Epic to make sure they are correct and make suggestions of things to change to keep the work in scope.

Initially, we tried generating the stories as part of the Planning meeting, but that proved too cumbersome. The stories and tasks are now generated beforehand by the engineering leadership. Generating the initial stories in this way is a temporary solution. Ideally, the team should generate the stories and tasks themselves.  

# Challenges 

Our current process is the result of iteration and continuous improvement. There are still some challenges to resolve.

One of the biggest challenges we need to resolve has to do with the time difference between the Seattle and remote teams. While a good backlog and prioritization in any agile process require ongoing grooming, having the teams working hours off of each other means that there is a lot of daily grooming work. Especially since new cards are being added every day by developers breaking down stories, Product Managers adding incremental changes, or bugs coming in. If there are a couple of days without dedicated effort on the backlog, developers can find themselves not being sure what to work on next. Our best solution to the problem so far is to empower the lead developer, who is remote, to be able to update the board to unblock developers there as needed.

Another challenge is making sure that all teams are using the process consistently. We've had a few issues with the shared board contained too many stories in the In Progress or To Do columns because one team wasn't using the same criteria as the rest of the organization. Doing some internal documentation and training has mostly addressed this problem.

Our most frequent issue is that the Done column on the detailed Kanban board can get full when we are working on a new feature or service. Since creating and deploying a new release is what moves the stories off the board, the Done column can get long at times. Having an overly-full column on the Kanban board makes it harder to understand the current state of the world (also in Jira it can mean much scrolling). We're working to get our feature-flagging architecture going which will allow us to release new functionality before exposing it to our customers. As a side effect, this will help us clear out this column more frequently.

The last challenge is that there is still manual work to create releases for the projects that aren't directly tied to a repository to move the cards from those projects off of the Kanban board. Since there are not usually very many of these stories, a periodic manual release for each of these projects takes care of the issue. Eventually, we will automate this process.  

# Summary 

At AstrumU, we are using a simple Kanban agile process along with some of the Scrum ceremonies to help us organize, prioritize and track our work. We continue to iterate upon this process, but in its current state, it does a good job keeping the distributed product development and data teams informed and coordinated while making priorities, plans and completed work transparent to the rest of the company.  

# Acknowledgments 

I want to give credit to Fedya Skitsko who developed a lot of the early Kanban process and Jira structure that is the basis of our current process and structure.


*Originally published on [Puppies, Flowers, Rainbows and Kittens](https://blog.kevingoldsmith.com/2019/02/04/agile-at-astrumu-a-case-study/)*
