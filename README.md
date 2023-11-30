# DrumWorld
## Portfolio project 4: DrumWorld
DrumWorld is a blog for those who are interested in drums and drumming. On the blog the user will find news from the drumworld, lessons or where to get them, and guidance through material within drumming and best in test materials.

**So get into the music!**
Johan Lindelöf

[DrumWorld Blog](https://jlindeloef.github.io/onstage-music-school/)

[Github Repository](https://github.com/jlindeloef/drumworld)


![The responsive image.](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/On%20devices.png)

## About the website
### Project planning
I notice around my fellow musicians that it would be great to have a blog about drumming and what is happening in the drummer community. Therefore I landed in to create a blog for my fourth project at Code Institute where I´m attending the fullstack program. 

This is my first blog creation so first I needed to look at different blogs both of how to code and what I wanted in my blog. I looked at youtube and looked through some code I could find on the internet that matches what I wanted. I also brought with me knowledge from my diploma course in coding. I wanted an easy blog with posts regarding everything about drumming, so catalyzing the posts into different categories is a must so it's easy for the user to maneuver through. 

I have used Balsamiq to plan how the blog should look like. I did it with a very easy layout because I didn't know when I started how easy or hard my decisions would be to code the blog
Here is my rough plan: [Onstage Music School](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/Onstage%20music%20school.pdf)

To create and plan the structure of the blog I made a flowchart which takes me through the game and helps me with the coding. It shows the logic path throughout the game
and can help you when you read this readme.


### UX
The blog are for everyone who likes the drums!

### Users stories
- As a user I want to read and experience content in blog.
- As a user I want to navigate easy and quickly through the website.
- As a user I want to log in so that I can take part of the content.
- As a user I want to make comments so that I can interact with the site.
- As a user I want to like/unlike post so that I can interact with the post.
- As a user I want to delete/edit comments so that change or regret.
I want to give the user a blog where they can find relevant content regarding drumming.

## Website structure
**When logged out:**
+ **DrumWorld/Home:** The logo and "Home" link will always take you back to the main page which is the post page.
+ **Sign Up:** For the user to sign up to get access to the whole blog content.
+ **Sign in:** For the user to log in and get access to the whole blog.
+ **Main page:** Here the user finds the posts. The user can click on the post to be redirect to the whole post content.
+ **Footer:** With contact information and links to social media.

**When logged in:**
+ **DrumWorld/Home:** The logo and "Home" link will always take you back to the main page which is the post page.
+ **Log Out:** When the user wants to log out from the blog.
+ **Categories:** To choose from different categories about drums.
+ **Main page:** Here the user finds the posts. The user can click on the post to be redirect to the whole post content. When logged in the user can Create/edit/delete and like posts.
+ **Footer:** With contact information and links to social media.

### Colours
 **Background:** I decided to use white background with lightseagreen to the navigation bar and footer. The lightseagreen will also be used on buttons and links. The text is in black and in the navbar and footer turns white when hovering over them. The function buttons are with a lightseagreen with black text and most of them turn white with black background when hovering over. The delete icon is red and gets a black background when hovering over. Also the delete button gets a red border when hovering over. Both the delete functions contain red to get a sense of a warning. The links are in black text and turn lightseagreen when hovering over it.

**The colors used was:**
**The colors used was:**
+ Lightseagreen #20b2aa - For navigation bar,footer and buttons.
+ Blue #10a4e8 - Like button.
+ White #FFF - used for background and text.
+ Black #000 - For text,border and background on buttons.
+ Red #ff0000 - Delete icon and delete border.
+ Grey #008000 - Borders.

### Technologies
1. HTML - To create a basic site.
2. Python/Django - To create most of the blog.
3. CSS - To create a nice, standout front-end and to give a great user experience.
4. Javascript - To create some functions.
5. Balsamiq - To create a wireframe.
6. app.diagram.net - To create the flowchart.
7. Gitpod to write the code.
8. github to store the code.

## Features

### Existing Features
I have divided the feature section into two parts. What features depend on if you are:
- Logged out
  **or**
- Logged in

#### ***When logged out:***
+ #### Navigation Bar
  - **DrumWorld/Home:** The navigation bar will view a title of the blog “DrumWorld” and a “Home”- link. Both of these are links to the home page from wherever you are on the webpage.
  - **Sign Up:** For the user to sign up to get access to the whole blog content.
  - **Sign in:** For the user to log in and get access to the whole blog.
Both "Sign Up" and "Sign In" will give a message if it succed or not.

+ #### Main page
  - Here the user finds the posts. The user can click on the post to be redirected to the whole post content and only read.
  - Every published post has an image, author of the post and when published.
  - Recent published post displays as the first post.

+ #### Footer
  - In the footer users find links to our social media.

#### ***When logged in:***
+ #### Navigation Bar
  - **DrumWorld/Home:** The navigation bar will view a title of the blog “DrumWorld” and a “Home”- link. Both of these are links to the home page from wherever you are on the webpage.
  - **Log Out:** **Log Out:** When the user wants to log out from the blog. The user will be redirected to a new page where user confims logging out.
  - **Categories:** The user can through the dropdown menu choose from different categories that the user wants to display. When the choice is made, only the posts in that category will view.

+ #### Main page
except what the user can do when logged out, the user can:
  - Create a comment that will display after approval from the admin.
  - The user can like a comment with the like-button under the post.
  - The user can edit and delete their own comment.
  - When editing a comment the user will be redirected to a page where the user can update the comment.
  - When the user wants to delete a comment the user will be redirected to a page where the user can confirm the deletion or cancel.


+ #### Footer
  - In the footer users find links to our social media.


### Features to Implement
Further there could be an about Us page and a direct contact to the admin. Also maybe create modals for sign in, sign up, log out, for edit/delete comment.


