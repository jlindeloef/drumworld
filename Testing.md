# Testing #

## Automated testing ##
| Page | Screenshot | Notes |
| --- | --- | --- |
| CSS | |  |  |
| CSS | ![CSS](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/CSS%20Valid.png) | Pass |
|HTML | |  |  |
| base.html and index.html | ![base,index](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/base.html%20and%20index.html.png) | Pass |
| post_detail.html | ![](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/post_detail%20html%20validation.png) | Pass |
| edit_comment.html | ![Edit](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/edit%20comment%20validation.png) | Pass |
| delete_comment.html | ![](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/delete%20comment%20validation.png) | Pass |
| signup.html | ![](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Sign%20up%20validation.png) | Pass |
| signin.html | ![sign in](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/Signin%20html%20validaded.png) | Pass |
| logout.html | ![log out](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/log%20out%20html%20validation.png) | Pass |
| category.html | ![category](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/category%20validation.png) | Pass |
|Javascript | |  |  |
| Javascript views current year | ![Javascript](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/javascript.png) | Pass |

## Manual testing ##
Full testing was made on the following devices:

- Laptop:
  - Macbook Pro 2022 14 inch screen
  - Samsung 2023 15 inch screen
- Mobile devices:
  - Iphone SE 2020
    
### Testing userstories ###
| Goals | How are they achieved? | images |
| --- | --- | --- |
| CSS | ![CSS](https://github.com/jlindeloef/drumworld/blob/main/static/images/images_readme/CSS%20Valid.png) | Pass |
| base.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| index.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| post_detail.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| edit_comment.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| delete_comment.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| signup.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| signin.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| logout.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |
| category.html | Show file differences that **haven't been** staged | Show file differences that **haven't been** staged |

### Full testing ###

| Feature | Expected Outcome | Testing Performed | Result | pass/failed |
| --- | --- | --- | --- | --- |
| Navbar | |  |  |
| Drumworld logo | When clicked the user will be redirected to the home page. | Clicked Logo and Home-link | Redirected to the home page. |Pass |
| Home-link | When clicked the user will be redirected to the home page. | Clicked Home-link | Redirected to the home page. |Pass |
| Sign Up link | When clicked the user will be redirected to the Sign up page. | Clicked Sign up-link | Redirected to the  Sign up page. |Pass |
| Sign In link | When clicked the user will be redirected to the Sign in page. | Clicked Sign In-link | Redirected to the Sign in page. |Pass |
| Log Out link | When clicked the user will be redirected to the Log out page. | Clicked Log out-link | Redirected to the Log out page. |Pass |
| Category Dropdown menu link | When clicked the category alternatives displays | Clicked Category-link | The alterenatives displays. |Pass |
| Category items | When clicked the categories display the chosen posts in that category | Clicked Categories | The post in that category displays. |Pass |
| Footer | |  |  |
| Social media links | When clicked the user will be redirected to the social medias website. | Clicked on all the social medias | Redirected to their website. |Pass |
| Signup page | |  |  |
| Sign Up button | When clicked the user will be redirected to the home page and submit form. | Clicked Sign up-button | Redirected to the  home page. |Pass |
| Username input - empty |This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required. |Pass |
| Password input - empty |This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required. |Pass |
| Email input - empty |This is not arequired field so the form should submit if empty | Tried to submit the form with this field empty | The form submits anyway |Pass |
| Signup page | |  |  |
| Sign In button | When clicked the user will be redirected to the home page and submit form. | Clicked Sign up-button | Redirected to the  home page. |Pass |
| Username input - empty |This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required. |Pass |
| Password input - empty |This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required. |Pass |
| Log Out page | |  |  |
| Log Out button | When clicked the user will be redirected to the home page signed out. | Clicked Log Out-button | Redirected to the  home page signed out. |Pass |
| Post page (Home) | |  |  |
| Link to individual post | When clicked the user will be redirected to a page to view the whole content of the post | Clicked the post link | Redirected to the the individual post page |Pass |
| Add comment | |  |  |
| Add comment button | When clicked the user will submit the made comment and an alert will show "Your comment is awaiting approval"| Clicked the Add comment-button | submits and view message |Pass |
| Add comment | |  |  |
| Add comment button | When clicked the user will submit the made comment and an alert will show "Your comment is awaiting approval"| Clicked the Add comment-button | submits and view message |Pass |
| Add comment button- no value entered |The form requires this field be filled in before submission|Left input blank | Tooltip lets me know this field is required |Pass |
| Edit comment | |  |  |
| Edit Icon |  When clicked the user will be redirected to the editpage to edit. | Redirect to edit page |Pass |
| Edit button | When clicked the user will be redirected to the individual post page with the uppdated comment in comments. | Clicked Edit-button | Redirected to the individual post page with the uppdated comment in comments. |Pass |
| Edit button- no value entered |The form requires this field be filled in before submission | Left input blank | Tooltip lets me know this field is required |Pass |
| Delete comment | |  |  |
| Delete Icon |  When clicked the user will be redirected to the Delete page to edit. | Redirect to Delete page |Pass |
| Delete button | When clicked the user will be redirected to the individual post page with the deleted comment deleted | Clicked Delete-button | Redirected to the individual post page with the the deleted comment deleted. |Pass |
| Cancel button | When clicked the user will be redirected to the individual post page | Clicked Cancel-button | Redirected to the individual post page. |Pass |









