# Scents Haven Blog

![Screenshot 2024-12-12 032117](https://github.com/user-attachments/assets/5539aec0-2854-47ee-b680-b8c25019af37)



## Live website

Link to live website: [Scents Haven]()

For Admin access with relevant sign-in information: [Scents Haven Admin](https://8000-zazamasilo-scentshaven-dj01lpb9cda.ws.codeinstitute-ide.net/admin/)
> 
> Welcome to my perfume blog, a fragrant space where I explore the captivating world of scents. Here, you’ll find engaging posts about various perfumes, fragrance families, and tips for enhancing your scent journey. Readers are encouraged to share their thoughts and experiences in the comments section of each post, fostering a vibrant community of fragrance enthusiasts. 
---
> 



>
---





## Table of contents
 - [User experience (UX)](#user-experience)
     - database planning
     - purpose and intended audience		 
     - user stories
 - [Creation process](#creation-process)
		 
     - [Wireframes](#wireframes)
 - [Design](#design)
		 
     - Colour scheme
		 
     - Typography
		 
     - Imagery
 - [Website features](#website-features)
 - [Tablet/mobile view](#tablet/mobile-view)
 - [Future features](#future-features)
 - [Technologies used](#technologies-used)
 - [Deployment](#deployment)
 - [Testing](#testing)
 - [Credits](#credits)
 ---

 ## USER EXPERIENCE
 ---
**Database Planning**

I used [LucidChart](https://lucid.app/documents#/documents?folder_id=recent) to create my ERD for my database. It is a model with six models: User, Post, Comment, Category,booking and collaboration request.

![ERD diagram](https://github.com/user-attachments/assets/6044f020-ee91-42dd-bd4e-ed2e70a85915)

**Purpose and Intended Audience**

**Purpose of Scents Haven**

The purpose of Scents Haven is to explore and celebrate the art of perfumery, providing fragrance enthusiasts with insightful reviews, tips, and guides. Our blog aims to inspire readers to discover their unique scents while fostering a community where they can share their experiences and passion for perfumes. We believe that every fragrance tells a story, and through our content, we strive to enhance your olfactory journey and promote sustainable practices in the world of beauty. 


**User stories**
		 
| User story | MoSCoW prioritisation |
| --- | --- |
| As a **User** I can **use a navigation links** so that **access other areas of the site easily** | Must have |
| As a **user** I can **click the home page icon** so that **I can quickly and easily return to the home page** | Must have |
| As a **user** I can **click on the about page link** so that **find out more information about the site** | Must have |
| As a **user** I can **navigate the social links** so that **connect with the site via social media** | Must have |
| As a **user** I can **open a blog post** so that **I can get the full information on a post I am interested in** | Must have |
 | As a **user/admin** I can **view comments on individual posts** so that **I can follow the conversation** | Must have |
 | As a **user/admin** I can **comment on posts** so that **I can take part in the conversation and be a part of the community** | Must have |
 | As a **user** I can **edit or delete my comments on a post** so that **I can be involved in the conversation and community** | Must have |
 | As a **user** I can **use my email and a password to register an account** so that **I can interact with the community and leave comments on posts** | Must have |
 | As a **site admin** I can **moderate user comments** so that **nothing inappropriate or offensive is added to the site** | Must have |
 | As a **user** I can **filter the blog posts based on their category** so that **see posts that match my interests** | Could have |
 | As a **site admin** I can **create new blog posts** so that **my audience has up to date and new content to enjoy** | Must have |
 | As a **site admin** I can **edit or delete blog posts** so that **users have the correct content and mistakes can be rectified** | Must have |
 | As a **site admin** I can **create and assign post categories** so that **users are able to filter the blog posts for a more tailored experience** | Could have |
 | As a **user** I can **search for blog posts using keywords** so that **get the specific information I need more quickly** | Could have |
 | As a **user** I can **see the most recent posts in a sidebar** so that **I have access to the most recent information quickly** | Won't have |
 | As a **user** I can **share posts on social media platforms** so that **I can interact with other users and a wider community** | Won't have |
 | As a **user** I can **create a booking** so that **I can have fragrance tryouts** | Must have |
 | As a **user** I can **view paginated list of posts** so that **I can choose what to read** | Must have |

 ## CREATION PROCESS

  ### Wireframes
  I created the wire frames using Figms. All login and registration forms were created by allauth and as such I haven't provided wire fr

### Mobile
![Rectangle 8](https://github.com/user-attachments/assets/46931943-31f3-4a6f-b683-dc1df3bd5006)


### Ipad and Desktop



## DESIGN
  - **Typography**
    
    [Google Fonts](https://fonts.google.com/) I decided to use two different fonts to distinguish between the general site text and the personal blog content. To achieve this, I imported the following font:
    The Playfair Display font was chosen as it is a visually appealing font for a perfume blog and easy to read.
    The Lato font was chosen as it is suitable for both body text and large headings. It would complement the Playfair Display font.S
    
  - **Colour scheme**
    
  ![Colour Pallete](https://github.com/user-attachments/assets/895e5188-17ea-4320-8933-65425027cbfa)

        
   Since my blog focuses on the world of perfume, I wanted the color scheme to reflect the elegant and vibrant hues found in the fragrance industry. I opted for strong, primary colors to create a striking contrast against a white background, ensuring that the overall design is impactful. However, I kept the palette limited so that it would not overshadow the beautiful images of perfumes and their intricate bottles, allowing the visuals to take center stage.
    The palette was chosen using [Coolers](https://coolors.co/)
    
  - **Imagery**
    
    The images used in each blog post are from [Pexels](https://www.pexels.com/) 
 


 ---

 ## WEBSITE FEATURES
 
   ### Main View

 <img width="277" alt="image" src="https://github.com/user-attachments/assets/656122c4-3d9f-461c-a233-ab1a7f3f732c" />

  I decided to have users arrive directly on the blog post page rather than requiring them to log in or register before being able to see anything. 
  I felt it would draw people in more and encourage them to then register and get involved.
  There are clear messages to tell the user whether they are logged in or not
  
  ### Signup feature

<img width="898" alt="image" src="https://github.com/user-attachments/assets/2165a9fd-e432-42d8-b422-0af910153300" />

Incorporating a signup feature would not only enhance user engagement but also helps cultivate a loyal readership and grow my blog's reach.

### Booking feature

<img width="652" alt="image" src="https://github.com/user-attachments/assets/4da7b7db-0a60-4eff-aea5-e764c95d60ca" />

<img width="565" alt="image" src="https://github.com/user-attachments/assets/e9ca4fd6-d92f-40d8-9ecd-c15fcbcbb091" />

I decided a  well-designed booking feature would contribute to a seamless user experience, making it easier for visitors to interact with the blog and access the services.





 


> 
> 

## FUTURE FEATURES
The following are some options to consider for inclusion in future versions of the website:
 - an option for users to create their own blog posts
 - A page for perfume reviews
 - A gallery page of popular fragrances with links to points of purchase
 ---

 ## TECHNOLOGIES USED

  ### Languages used
  - HTML5

  - CSS

  - JavaScript

  - Python
   - asgiref==3.8.1
   - cloudinary==1.41.0
   - dj-database-url==0.5.0
   - gunicorn==20.1.0
   - oauthlib==3.2.2
   - psycopg==3.2.1
   - PyJWT==2.9.0
   - python3-openid==3.2.0
   - requests-oauthlib==2.0.0
   - sqlparse==0.5.1
   - urllib3==1.26.19
   - whitenoise==5.3.0
     

  - Django
    - summernote==0.8.20.0
    - allauth==0.57.2
    - crispy-forms==2.3

  ### Frameworks, libraries and programs used

   
  1. [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
        - Bootstrap was used to ensure the site was responsive and for styling
  2. [Balsamiq](https://balsamiq.com/wireframes/)   
        - Balsamiq was used to produce the wireframes in the design phase.
  3. [Git](https://git-scm.com/)
        - Git was used for version control
  4. [Github](https://github.com/)
        - GitHub was used to store the code and allow collaboration on the project.
  5. [StackEdit](https://stackedit.io/)
        - StackEdit was used to assist with the markdown in the README.md
  6. [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools)
        - Used to troubleshoot and test design ideas and styling.   
  7.  [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)  
        - used to test performance of the website
  8. [Favicon](https://favicon.io/)
        - used to generate the favicon  
  9. [W3 Schools](https://www.w3schools.com/)
        - used to look up syntax for HTML and CSS
  10. [Stack Overflow](https://stackoverflow.com/)                  
        - used for queries around coding
  11. [Perplexity](https://www.perplexity.ai/)    
        - used to provide sources to generate text for the website   
  12. [Font Awesome](https://fontawesome.com/)    
        - used for the favicon
  13. [Pexels](https://www.pexels.com/)
        - used for copyright free images
  14. [W3C HTML validator](https://validator.w3.org/)
        - used to validate the HTML
  15. [W3 Jigsaw](https://jigsaw.w3.org/css-validator/)
        - used to validate the CSS
  16. [JSHint](https://jshint.com/)
        - used to validate the JavaScrip
  17. [Python Enhancement Proposals](https://peps.python.org/pep-0008/)
        - for advice on PEP8 compliance
  18. [Free Code Camp](https://freecodecamp.org)   
        - for help with JavaScript concepts and syntax 
  19. [Django framework](https://www.djangoproject.com/)
  20. [Django Project - Build a simple blog tutorial](https://www.youtube.com/watch?v=S9-Bt1JgRjQ&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&index=5)
  21. [CI Python Linter](https://pep8ci.herokuapp.com/) - for validating Python code
  22. [Heroku](https://dashboard.heroku.com/apps)



 ---

 ## DEPLOYMENT
 The site was deployed to Heroku. The steps to deploy are as follows:
 - Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
 - In the Procfile write 'web: gunicorn scents haven.wsgi'
 - In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
 - In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list, git add, commit and push to github

Navigate to the Heroku dashboard
 - Create a new Heroku app
 - Give it a name and select the region 'Europe'
Navigate to settings tab and scroll down to Config Vars
 - Click 'Reveal Config Vars'
 - Add the following keys:
         key = DATABASE_URL | value = (my secret database url)
         key = SECRET_KEY | value = (my secret key)
Navigate to Deploy tab
 - Connect to GitHub and select the repo 'lunar-lists'
 - Scroll down to 'Manual deploy' and select the 'main' branch
 - Click 'Deploy Branch'
   

 ## TESTING

  ### HTML validation
  I have used the W3C Markup validator to validate all of my HTML code - [W3C Markup Validator](https://validator.w3.org/)

A different approach was required for validating the HTML for this project as all of the pages are developed using DTL and most require user authentication. The HTML validator will throw errors if I were to use the URL so I have had to follow the below approach for every page:
  - navigate to the deployed Heroku link
  - right click to find the 'view page source' link
  - copy and paste the HTML code from here into the validator via the direct input

![Screenshot 2024-12-12 114704](https://github.com/user-attachments/assets/3d160f1d-bdc5-47e7-919f-a44f4f533047)

All HTML was checked and had no errors or warnings to show as indicated above. 

  ### CSS validation

<img width="920" alt="image" src="https://github.com/user-attachments/assets/cbb68fde-1a20-42a1-8f71-ebcf557f39b3" />
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file. 
All CSS checked and had no errors or warnings to show as indicated above.

 ### Javascript validation

  [JavaScript Validator](https://jshint.com) - The JavaScript code passed the validation process without any errors being detected. The use of let and const to define variables and template literals is only available with ES6 was highlighted.

   ### Python validation
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the python files I created or edited myself.
Initial errors were shown involving indentation and spacing but these were corrected.    

  

## Lighthouse scores via Chrome dev tools 
<img width="388" alt="image" src="https://github.com/user-attachments/assets/aa6110fe-4857-449f-9b8c-728cc27a1edc" />



The performance score is low due to image formats. Image formats like WebP and AVIF often provide better compression than PNG or JPEG, which means faster downloads and less data consumption.





