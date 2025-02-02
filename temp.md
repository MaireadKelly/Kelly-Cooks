# Scrum-diddly-umptious

## Overview

Scrum-diddly-umptious provides an easy and engaging way to explore, share, and manage recipes. With a focus on user interaction, the site offers robust CRUD functionalities that allow registered users to create, read, update, and delete recipes. The site is designed with a mobile-first approach to ensure a seamless experience across all devices, utilizing responsive design frameworks like Bootstrap.

**Live Link:** https://kellycookspp4-63d6db43ef5f.herokuapp.com/
**Link to GitHub Repository**

![Site Mock-up](static/documentation/readme/responsive.png)

## Features

**Existing features:**

- **Homepage Overview:**
  - **Featured Recipes:** The homepage displays a selection of featured recipes along with brief descriptions and images.
  - **Navigation:**   The navigation menu is featured on all pages to provide a consistent means of navigating the site. The menu provides links to 'Home' page, 'Browse' page, 'My Recipe Book' page, 'Create Recipe' page, a login link when the user is unauthenticated and a logout link when the user is authenticated. It is fully responsive, collapsing into a navbar toggle button which presents the navigation menu as a dropdown menu. A navbar brand and image features on the left of the navbar, providing an additional link to the 'Home' page.

    ![NavBar](static/documentation/readme/nav-bar.png)
    ![NavBar](static/documentation/readme/nav-bar.png)



  - **Recipe Cards:** Each recipe is presented in a card format, offering a snapshot of the dish with a link to view full details.
  ![Main](static/documentation/readme/home-main.png)
  ![Features-Recipes]

- **User Account System:**
  - **Registration & Login:** Users can sign up for an account, log in, and manage their own recipes.
  - **Profile Management:** Registered users have personal profiles where they can view and edit their submitted recipes, And view their Favourite Recipes

  ![Register](static/documentation/readme/register.webp)
  ![Login](static/documentation/readme/login.webp)

- **Recipe Management (CRUD):**
  - **Upload Recipes:** Users can create and upload new recipes with details such as ingredients, description, instructions and images.
  - **Review and Edit:** After submission, users can review, edit, or delete their own recipes.
  - **Comments & Ratings:** Users can leave reviews on other users recipes to share their feedback and tips.

  ![Recipe Details](static/documentation/readme/recipe-details.webp)
  ![Review Panel](static/documentation/readme/comments-panel.webp)

- **Search & Filter:**
  - **Recipe Search:** Easily search for recipes by keywords, Title or ingredients.
  
- **Responsive Design:**
  - The site is built with a mobile-first approach ensuring it is fully responsive on all devices, from desktops to smartphones.

- **Admin Panel:**
  - **Site Administration:** Admins can manage user accounts, moderate recipes and comments, and ensure the overall integrity of the platform using a built-in admin interface.
  - # User Stories for Django Admin Panel

| **USER STORY**                     | **DETAILS**                                                                                                                                                   | **ACCEPTANCE CRITERIA**                                                                                                                                                                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Manage Site Content**            | As a site administrator, I want to manage static site content so that users have access to up-to-date information.                                            | - Admin dashboard includes a section to view, edit, and update static site content pages.<br> - Admin can edit text and images for each static page.<br> - Changes are saved and immediately reflected on the live site.<br> - Formatting is accessible. |
| **Manage Recipes**                 | As a site administrator, I want to manage all submitted recipes to ensure the content meets the platform's quality and community guidelines.                  | - Admin dashboard displays a list of all recipes with search, filter, and sort features.<br> - Admin can view detailed information, approve or reject recipes, and edit recipe details.<br> - Notifications for new submissions are enabled.            |
| **View and Manage Reports**        | As a site administrator, I want to view and manage user-generated reports to address issues promptly and maintain a safe environment.                         | - Admin dashboard displays reports submitted by users.<br> - Admin can take appropriate actions based on the report.<br> - Notifications for new reports are enabled.                                                                                   |
| **Monitor Platform Activity**      | As a site administrator, I want to monitor platform activity to keep track of user engagement and identify any issues.                                        | - Admin dashboard provides an overview of metrics (e.g., active users, new registrations, reviews submitted).<br> - Admin can access logs of user actions and filter by date, user, and action type.<br> - Alerts for unusual activity.                  |

 
[Admin-Panel]

|------------------------------------------------------------------------------------------|

  # User Stories for Main Application

# User Stories for Front End (User-Facing)

| **USER STORY**                     | **DETAILS**                                                                                                                                                   | **ACCEPTANCE CRITERIA**                                                                                                                                                                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Deploy the App**                 | As a developer, I want clear deployment instructions so that the app can be cloned and run locally.                                                           | - README includes all deployment steps.<br> - Covers running migrations, installing requirements, and setting up `.env`.                                                                                                                                 |
| **Social Media Links**             | As a user, I want social media links in the footer so that I can follow the website's social pages.                                                           | - Footer contains links to all relevant social media platforms.<br> - Clicking on an icon opens the respective page in a new tab.                                                                                                                         |
| **404 Page**                       | As a user, I want a custom 404 page so that I get clear feedback when a page doesn't exist.                                                                   | - Custom 404 page for non-existent URLs.<br> - Page matches the site's theme.                                                                                                                                                                             |
| **User Authentication**            | As a user, I want secure authentication so that my account and data are protected.                                                                            | - Registration and login functionality.<br> - Restricted page access without logging in.<br>                                                                                                                                 |
| **Add Recipe Review**              | As a user, I would like to be able to comment on my and other members' recipes.                                                                               | - Create comment functionality.<br> - Submit comments.                                                                                                                                                                                                   |
| **Add Cancel Button to Delete Recipe** | As a user, I would like to have the option to cancel before deleting a recipe.                                                                                | - Cancel option before deleting recipes.<br> - Confirmation prompt before finalizing the action.                                                                                                                                                         |
| **Browse and Search for Recipes**  | As a user, I want to browse and search for recipes so that I can find something I'd like to cook.                                                             | - Homepage displays a list of recipes with titles, images, and brief descriptions.<br> - A search bar allows users to search recipes by keywords.<br> - Clicking a recipe navigates to a detailed view page with full recipe details.                     |
| **Login and Out**                  | As a user, I can login and out of the website so that I can access my personalized features.                                                                  | - Users must be able to log in using their registered email and password.<br> - Invalid login attempts display an error message.<br> - Successful login redirects users to a dashboard or homepage.<br> - Logout redirects to homepage.                   |
| **User Registration**              | As a user, I can register an account so that I can log in and save my favorite recipes.                                                                       | - Users must be able to register with a unique email and password.<br> - Registration includes validation (e.g., email format, password strength).                                                                                                       |


**Future Features:**

# Future Features for Consideration

| **USER STORY**                     | **DETAILS**                                                                                                                                                   | **ACCEPTANCE CRITERIA**                                                                                                                                                                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Add Servings**                   | As a site user, I want to see how many servings a recipe will produce so that I know how much food I will have.                                               | - Acceptance criteria to be defined.                                                                                                                                                                                                                     |
| **Manage Advertisements and Promotions** | As a site administrator, I want to manage advertisements and promotions to generate revenue and enhance user engagement.                                     | - Admin dashboard provides a section to manage advertisement placements and banners.<br> - Admin can upload and schedule ads.<br> - Admin can track ad performance metrics.                                                                             |
| **User Story Backup and Restore Site Data** | As a site administrator, I want to back up and restore site data to prevent data loss and ensure quick recovery in case of issues.                            | - Admin dashboard includes options for manual and automated backups.<br> - Admin can schedule regular backups and view backup logs.<br> - Admin can restore the site to a specific backup with confirmation.                                             |
| **Manage Notifications and Announcements** | As a site administrator, I want to send notifications and announcements to users to keep them informed about updates and news.                                | - Admin can create, schedule, and send notifications to users via email or in-app.<br> - Notifications are displayed consistently across all devices.                                                                                                   |
| **View and Manage Reports**        | As a site administrator, I want to view and manage user-generated reports to address issues promptly and maintain a safe environment.                         | - Admin dashboard displays reports submitted by users.<br> - Admin can take appropriate actions based on the report.<br> - Notifications for new reports are enabled.                                                                                   |
| **Monitor Platform Activity**      | As a site administrator, I want to monitor platform activity to keep track of user engagement and identify any issues.                                        | - Admin dashboard provides an overview of metrics (e.g., active users, new registrations, reviews submitted).<br> - Admin can access logs of user actions and filter by date, user, and action type.<br> - Alerts for unusual activity.                  |
| **Recipe Collections**             | As a user, I want to create personal recipe collections or meal plans so that I can organize and save my favorite recipes.                                    | - Users can create collections or meal plans.<br> - Recipes can be added or removed from collections.<br> - Collections can be named and saved for later use.                                                                                          |
| **Social Sharing**                 | As a user, I want to share recipes directly to social media platforms so that I can share them with friends and family.                                        | - A "Share" button is displayed on each recipe.<br> - Users can select social media platforms to share recipes.<br> - The shared recipe includes a link back to the website.                                                                             |
| **Advanced Filtering**             | As a user, I want more granular filtering and search options so that I can easily find recipes that meet my preferences.                                      | - Filters for dietary restrictions, ingredients, cooking time, etc.<br> - Filters are dynamically adjustable and work in conjunction with the search bar.                                                                                                                                       |

This project was developed using Agile methodology which allowed me to iteratively and incrementally build my app, with flexibility to make changes to my design throughout the entire development process.

GitHub Issues and Projects were used to manage the development process. Each part of the app is divided into Epics_ (Milestones) which are broken down into User Stories (Issues) with Tasks (Acceptance Criteria). An Epic represents a large body of work, such as a feature. The board view of the Project feature was used to display and manage my progress in the form of a 'kanban board'. The user stories were added to the 'Todo' column to be prioritised for development, moved to the 'In Progress' column to indicate development of the feature had begun and finally moved to the 'Done' column when the feature had been implemented and the acceptance criteria had been met.

![Kanban Board](docs/images/kanban.png)

User stories were prioritised using the MoSCoW prioritisation technique. Each user story was given one of the following labels:

- Must have - to indicate the user story is guaranteed to be delivered.
- Should have - to indicate the user story would add significant value but is not vital.


Our process was guided by the MOSCOW framework:
- **Must have:** Core features like recipe submission, user registration, and full CRUD functionality.
- **Should have:** Features such as recipe search and filtering.
- **Could have:** Advanced features like recipe collections and social sharing.
- **Won't have:** Features planned for future updates.

[The Project Kanban Board](https://github.com/users/VictoriaParkes/projects/2)

### Project Issues

![Project Issues](static/documentation/readme/issues.webp)
<!-- Replace with your own screenshot if available -->


## User Stories

User stories were instrumental in defining the scope and functionality of the project.

| **USER STORY**                   | **DETAILS**                                                              | **ACCEPTANCE CRITERIA**                                          |
| -------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Submit a Recipe**              | As a user, I can submit a new recipe so that I can share my culinary creations. | (1) A form is provided for recipe submission. (2) The recipe appears in my profile after submission. |
| **Browse Recipes**               | As a user, I can browse all recipes to find new meal ideas.             | (1) Recipes are listed on the homepage with a preview.            |
| **Rate and Comment**             | As a user, I can rate and comment on recipes to share feedback.         | (1) Only logged-in users can leave reviews. (2) Comments show the user's name and timestamp. |
| **Edit or Delete Recipe**        | As a user, I can update or delete my own recipes.                        | (1) Users see edit/delete options only on their own recipes.       |

<!-- Add more user stories as necessary -->

## Site Testing

For detailed testing procedures and results, please refer to the [TESTING.md](TESTING.md) document.

## UX/UI Wireframing

- **Design and Aesthetic:**
  - The site employs a clean, modern design with a focus on readability and ease of use.
  - A custom color palette and typography enhance the user experience and brand identity.

- **Navigation and Interaction:**
  - The navigation bar is designed for ease of access, ensuring users can find recipes, submit their own, and navigate their profiles effortlessly.

### Wireframe

![Wireframe](static/documentation/readme/wireframe.webp)

### UI Colour Palette

![UI Colour Palette](static/documentation/readme/colours.webp)

## Technologies Used

### Languages & Frameworks

- **Frontend:**
  - HTML5/CSS3
  - Bootstrap (for responsive design)
  - JavaScript (for interactivity)

- **Backend:**
  - Django Framework (Python) for server-side logic and database management

### Libraries & Tools

- Django vX.X.X
- [Additional libraries such as Django AllAuth, Django Crispy Forms, etc.]
- Cloudinary (for media storage)
- PostgreSQL (for the database)

### External Resources

- **Testing & Validation:**
  - HTML: [W3C Validator](https://validator.w3.org/nu/)
  - CSS: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - JavaScript: [JSHint](https://jshint.com/)
  - Accessibility: [WAVE](https://wave.webaim.org/)

## Django Project Setup

1. **Install Django and Required Libraries:**

   ```bash
   pip3 install django gunicorn
   pip3 install dj-database-url psycopg2
   pip3 install cloudinary
