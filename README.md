# DrumWorld
## Portfolio project 4: DrumWorld
DrumWorld is a blog for those who are interested in drums and drumming. On the blog the user will find news from the drumworld, lessons or where to get them, and guidance through material within drumming and best in test materials.

**So get into the music!**

Johan Lindelöf

[DrumWorld Blog](https://drumworld-9b0612a3caf4.herokuapp.com/)

[Github Repository](https://github.com/jlindeloef/drumworld)


![The responsive image.](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/On%20devices.png)

## About the website
### Project planning
I notice around my fellow musicians that it would be great to have a blog about drumming and what is happening in the drummer community. Therefore I landed in to create a blog for my fourth project at Code Institute where I´m attending the fullstack program. 

This is my first blog creation so first I needed to look at different blogs both of how to code and what I wanted in my blog. I looked at youtube and looked through some code I could find on the internet that matches what I wanted. I also brought with me knowledge from my diploma course in coding. I wanted an easy blog with posts regarding everything about drumming, so catalyzing the posts into different categories is a must so it's easy for the user to maneuver through. 

I have used Balsamiq to plan how the blog should look like. I did  a very easy layout because I didn't know when I started how easy or hard my decisions would be to code the blog.
Here is my rough plan: [Drumworld wireframe](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Drumworld-wireframe.png)

To create and plan the structure of the blog I made a flowchart which takes me through the site and helps me with the coding. It shows what the user gets when visiting the blog
and can help you when you read this readme.

![Flowchart](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/logic%20chart.drawio.png)


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

### ***When logged out:***
+ #### Navigation Bar
![Navbar logged out](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/navbar%20kogged%20out.png)
  - **DrumWorld/Home:** The navigation bar will view a title of the blog “DrumWorld” and a “Home”- link. Both of these are links to the home page from wherever you are on the webpage.
  - **Sign Up:** For the user to sign up to get access to the whole blog content.
  - **Sign in:** For the user to log in and get access to the whole blog.

![Sign up](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Signup.png)![](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/signin.png)
  

Both "Sign Up" and "Sign In" will give a message if it succed or not.


+ #### Main page
  - Here the user finds the posts. The user can click on the post to be redirected to the whole post content and only read.
  - Every published post has an image, author of the post and when published.
  - Recent published post displays as the first post.
  
 ![A post](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/apost.png)
+ #### Footer
  - In the footer users find links to our social media.
 
![Footer](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/footer.png)

### ***When logged in:***
+ #### Navigation Bar
![Navbar logged in](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/navbar%20logged%20in.png)
  - **DrumWorld/Home:** The navigation bar will view a title of the blog “DrumWorld” and a “Home”- link. Both of these are links to the home page from wherever you are on the webpage.
  - **Log Out:** When the user wants to log out from the blog. The user will be redirected to a new page where user confims logging out.
    ![Log out](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/logout.png)
  - **Categories:** The user can through the dropdown menu choose from different categories that the user wants to display. When the choice is made, only the posts in that category will view.
    ![Category dropdown](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/navbar-category-dropdown.png)

+ #### Main page
except what the user can do when logged out, the user can:
  - The user can like a post with the like-button under the post.
    
![Like](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Liked.png)
  - Create a comment that will display after approval from the admin. An alert will tell the user that admin needs to approve the comment.
    ![Commentfield](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/commentfield.png)
    ![Comments made](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Comments%20made.png)  
  - The user can edit and delete their own comment.

    ![Edit/delete](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Deleteedit.png)
  - When editing a comment the user will be redirected to a page where the user can update the comment.
    ![Edit](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Edit.png)
  - When the user wants to delete a comment the user will be redirected to a page where the user can confirm the deletion or cancel.
![Delete](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Delete.png)


+ #### Footer
  - The footer is the same as when logged out. It contains links to social media.


### Features to Implement
Further there could be an about Us page and a direct contact to the admin. Also maybe create modals for sign in, sign up, log out, for edit/delete comment.

## Testing
If you want to know more about my automated and manualy testing you can click [here.](https://github.com/jlindeloef/drumworld/blob/main/Testing.md)
+ I tested the site, and it works in different web browsers: Chrome, Firefox, and Microsoft Edge.
+ On mobile devices, I tested the blog on a Samsung Galaxy A13 with the Samsung browser and an iPhone SE with the Safari browser.
+ I confirmed that the site is responsive and functions on different screen sizes using the devtools device toolbar.
+ I confirmed that the blog readable and easy to understand.

### Validator Testing
+ HTML No errors were returned when passing through the official W3C validator.
+ CSS No errors were found when passing through the official (Jigsaw) validator.
+ Javascript No errors were found when passing through JSHint validator.
+ Python showed the same warning in two of the files which doesn´t effect the blog.

  ### Bugs
+ Solved bugs
  - The category dropdown menu in the navbar didn´t work.
  - The Edit and Delete confirmation buttons did not redirect to the postsite when pressing.
  - The Edit and Delete icons did not work individual for the comment writer.
  - The CSS did not view when deployed.
  All these bugs are fixed with help from the tutors at Code Institute. 
+ Unsolved bugs
  - No unsolved bugs.

   ## Deployment
I followed the steps written below to deploy my project to Heroku:
 + First created a Heroku account by flollowing the instructions given from Code Institute.
 + "Create new App".
 + Give the App an unique name and enter region europe.
 + Click on "Create App".
 + Go to Deploy section tab and scroll down to the Deployment Method.I connect to Github pages and then could search for my Github Repository "DrumWorld" and then click connect.
 + Scroll down to Automatic and Manual Deploys sections. I clicked on Manual Deployment.
 + Deploy Branch.
 + After the project has been deployed successfully I clicked the View-button to see the program run in the terminal.

In github:
The site was deployed to Git Hub pages using the following steps:
+ After logging into GitHub I located my repository for my Portfolio Project 4.
+ I then clicked the "Settings" button at the top of my repository
+ Under General, navigate to Code and Automation and select "Pages".
+ In the Build and Deployment section for Source, select 'Deploy from a branch' from the drop-down list.
+ For Branch, select "main" from the drop-down list and "/root" in the next bar and Save.
+ On the top of the page, the link to the complete website is provided.
+ The deployed site will update automatically upon new commits to the master branch.

  ## Credits
**Code:** Some code parts were taken from W3Schools (https://www.w3schools.com/), Stack Overflow (https://stackoverflow.com/) modified for the purpose of my website. 
Code used in "I Think Therefore I Blog" was used and changed for creating my blog.

### Acknowledgements
My mentor Medale Oluwafemi for guidance and inspiration and reviewing. Also a great thanks to Code Institutes tutors and Student support Who has been a great help during this project:
Ideas and inspiration were taken from The Code Institute's "I Think Therefore I Blog".

