# Recipe Sharing App

![Mockup Screenshots](static/documentation/readme/responsive.png)

Recipe Sharing App is an online platform designed for food enthusiasts and home cooks to share their favorite recipes. Users can browse through publicly available recipes, submit their own, and interact with the community by saving or commenting on recipes.

[Live Application](https://kellycookspp4-63d6db43ef5f.herokuapp.com/)

## Table of Contents:
1. [User Experience (UX)](#user-experience-ux)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
2. [Design](#design)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Libraries](#libraries-used)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgments](#acknowledgments)

---

## **User Experience (UX)**
On the home page the main section gives a brief description of the site and the clickable button changes between "Browse Recipes" or "Sign Up", based on whether the user is logged in or not so as to entice non registered visitors to sign up.

![Main Signed in](static/documentation/readme/signed-in.png)
![Main Not SIgned In](static/documentation/readme/not-signed-in.png)
### **User Stories**


#### **Navigation**
- As a user, I want a simple navigation menu to find content easily.
- As a user, I want the navigation menu to be accessible on all devices.
- As a user, I want to see social media links for community interaction.

#### **Core Functionality**
- As a user, I want to register an account to access features.
- As a user, I want to log in and out of my account securely.
- As a user, I want to browse and search for recipes easily.
- As a user, I want to add new recipes to share with others.
- As a user, I want to edit and delete my recipes when needed.
- As a user, I want clear cooking instructions for recipes.
- As a user, I want to review recipes.
- As an admin, I want to manage user accounts and reviews.

![Browse](static/documentation/readme/full-recipes.png)


#### **UI Improvements**
- As a user, I want a cancel button for delete and logout confirmations.
- As a user, I want social media links to connect with the community.
- As a user, I want a 404 error page for incorrect URLs.

![404 Error](static/documentation/readme/404.png)

#### **Navigation**
- As a user, I want a simple navigation menu to find content easily.
- As a user, I want the navigation menu to be accessible on all devices.
- As a user, I want to see social media links for community interaction.

#### **Recipe CRUD Operations**
- As a registered user, I want to submit recipes.
- As a user, I want to edit or update my submitted recipes.
- As a user, I want to delete my own recipes.

### **Admin Panel Functionality**
In the Djanggo Admin Panel authorised users can perform all CRUD operations on Users, Recipes and Reviews to keep the site a safe and friendly place for all.

![Admin Panel](static/documentation/readme/admin.png)
![Admin Delete](static/documentation/readme/admin-delete-user1.png)
![Admin Confirm Delete](static/documentation/readme/admin-delete-user2.png)
![Admin Delete Success](static/documentation/readme/admin-delete-user3.png)
![Admoin Edit Review](static/documentation/readme/admin-edit-review.png)

### **Wireframes**
![Wireframe Home](static/documentation/readme/home-d-wireframe.png)
![Wireframe Signup](static/documentation/readme/signup-d-wireframe.png)
![Wireframe Recipes](static/documentation/readme/recipes-d-wireframe.png)
![Wireframe Add Recipe](static/documentation/readme/add-recipe-d-wireframe.png)


### **Agile Methodology**
This project was developed using Agile methodology which allowed me to iteratively and incrementally build my app, with flexibility to make changes to my design throughout the entire development process.

GitHub Issues and Projects were used to manage the development process. Each part of the app is divided into Epics_ which are broken down into User Stories with Tasks. An Epic represents a large body of work, such as a feature. The board view of the Project feature was used to display and manage my progress in the form of a 'kanban board'. The user stories were added to the 'Todo' column to be prioritised for development, moved to the 'In Progress' column to indicate development of the feature had begun and finally moved to the 'Done' column when the feature had been implemented and the acceptance criteria had been met.

![Kanban Board](static/documentation/readme/kanban-view-1.png)

User stories were prioritised using the MoSCoW prioritisation technique. Each user story was given one of the following labels:

- Must have - to indicate the user story is guaranteed to be delivered.
- Should have - to indicate the user story would add significant value but is not vital.
- Could have - to indicate the user story would have a small impact if left out.
- Won't have - to indicate the user story is not a priority in the current iteration.

GitHub milestones were also used to group related user stories together.
Thankfully for this project all of the "Could Have" issues were completed.

![Must Have](static/documentation/readme/kanban-must-have.png)
![Should Have](static/documentation/readme/kanban-should-have.png)
![Won't Have](static/documentation/readme/kanban-view-5.png)

---

## **Design**

### **UI Colour Palette**

![UI Colour Palette](static/documentation/readme/colours.png)


## **Features**

### **Navigation Bar**
- Provides quick access to Home, Recipe List, Submit Recipe, and User Profile.
- Responsive on all screen sizes.

![NavBar Desktop View](static/documentation/readme/Nav-Bar-desktop.png)
![NavBar Mobile View](static/documentation/readme/Nav-Bar-Mobile.png)
![Footer](static/documentation/readme/footer.png)

### **Recipe Submission**
- Users can submit new recipes using a structured form.
- Recipes include images, ingredients, and step-by-step instructions.

![Add Recipe](static/documentation/readme/add-recipe.png)

### **Recipe Viewing & Management**
- Recipes can be saved in "My Recipe Book."
- Users can edit or delete their recipes.

![Edit Recipe](static/documentation/readme/edit-recipe.png)
![Delete Recipe](static/documentation/readme/delete-recipe.png)

### **Review Recipes**

![Add Review](static/documentation/readme/add-review.png)
![Edit Review](static/documentation/readme/edit-review.png)

### **Favourites**
- Users can add and remove recipes from their favourites so they can find them easily through their "My Recipes" link.
- Users can search for recipes by searching titles and ingredients

![Favourites Menu](static/documentation/readme/nav-my-recipes.png)
![Add to Favourites](static/documentation/readme/add-to-favourite.png)
![Favourite Recipes](static/documentation/readme/favourites-view.png)
![Search](static/documentation/readme/search.png)

### **User Authentication**
- Secure user login and registration.

![User Register](static/documentation/readme/sign-in.png)
![User Signin](static/documentation/readme/sign-up.png)
![User Signout](static/documentation/readme/sign-out.png)

---

## **Technologies Used**
- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Bootstrap
- **Hosting:** Heroku
- **Storage:** Cloudinary for image uploads

---

## **Libraries Used**
- Django
- Gunicorn
- Cloudinary
- dotenv
- PostgreSQL

---

## **Testing**
- **Manual Testing:** Validated all user stories through structured tests.
- **Google Lighthouse Performance:** Performance scores captured for mobile and desktop.
- **Browser Compatibility:** Verified across Chrome, Firefox, Edge.
- **Code Validation:** W3C Code Validator and PEP8 formatting were used.  CI Python Linter

For detailed testing results, refer to the [Testing Documentation](TESTING.md).

---

## **Bugs**
| Bug | Fix |
|------|------|
| Image upload failure | Adjusted Cloudinary API settings |
| Navigation not working on mobile | Updated Bootstrap layout |

---

## **Deployment**
### **Steps to Deploy on Heroku**
1. Create a repository on GitHub.
2. Set up Heroku and link to the repository.
3. Configure environment variables:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `CLOUDINARY_URL`
   - `PORT=8000`
4. Deploy manually through Heroku's interface.

---

## **Credits**
- Most recipes including images were sourced from https://www.bbcgoodfood.com/
- Icons sourced from FontAwesome.
- Fonts from Google Fonts
- Visily was used for Wireframe creation
- ChatGPT for help with error resolution and general code queries

---

## **Acknowledgments**
Special thanks to my Tutor Marko Tot and colleagues for their guidance. For Code Peer Reviewer Cam who took the time to review my project.
