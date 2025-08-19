# Kelly Cooks

Kelly Cooks is a recipe sharing web application where users can browse, share, edit, and review recipes.  
It provides an easy-to-use interface for both casual home cooks and food enthusiasts to connect and inspire each other.

![Kelly Cooks Home Page](docs/readme/ui-home.png)

---

## **UX**

### **Project Goals**
- Provide a platform for users to share their own recipes.
- Allow users to browse recipes by others and leave reviews.
- Include user authentication for adding/editing/deleting recipes and reviews.
- Make the interface clean, intuitive, and mobile-friendly.

---

### **Target Audience**
- People who love cooking and want to share recipes.
- Those looking for cooking inspiration.
- Users who want to interact with a community through recipe reviews and favourites.

---

## **Agile Development**

This project followed an Agile methodology, using a [GitHub Projects Kanban Board](https://github.com/users/MaireadKelly/projects/5/views/1) to manage development tasks and track progress.  
The board was divided into columns for **To Do**, **In Progress**, and **Done**, with user stories moved through the workflow as they were implemented and tested.

### **MoSCoW Prioritisation**
User stories were categorised into **Must Have**, **Should Have**, and **Could Have** based on importance and time constraints.

#### **Must Have**
- As a user, I can register for an account so that I can create and manage my own recipes.
- As a user, I can log in and log out so that I can access my account securely.
- As a user, I can add a recipe so that I can share it with others.
- As a user, I can edit my recipe so that I can update or correct it.
- As a user, I can delete my recipe so that I can remove it if necessary.
- As a user, I can browse recipes so that I can find cooking inspiration.
- As a user, I can review recipes so that I can share my feedback.
- As a user, I can mark recipes as favourites so that I can easily find them later.

#### **Should Have**
- As a user, I can search for recipes so that I can quickly find a recipe by keyword.
- As a user, I can view my own recipes so that I can manage them in one place.
- As a user, I can remove a recipe from my favourites list.

#### **Could Have**
- As a user, I can filter recipes by category so that I can find recipes by type.
- As a user, I can upload a profile picture to personalise my account.
- As a user, I can share recipes on social media.

---

## **Wireframes**
Wireframes were created to plan the layout and functionality of the application.

- **Home Page**  
  ![Home Page Wireframe](docs/readme/wireframe-home.png)
- **Recipe List**  
  ![Recipe List Wireframe](docs/readme/wireframe-recipe-list.png)
- **Recipe Detail**  
  ![Recipe Detail Wireframe](docs/readme/wireframe-recipe-detail.png)

---

## **Entity Relationship Diagram**
The ERD below illustrates the models and relationships used in the project.

![Entity Relationship Diagram](docs/readme/erd-diagram.png)

---

## **Features**

### **Implemented Features**
- User registration and login/logout functionality.
- Add, edit, and delete own recipes.
- Browse all recipes.
- Leave reviews on recipes.
- Mark recipes as favourites.
- Search functionality.
- Responsive design for mobile, tablet, and desktop.


### User Registration

New users can register an account using the sign-up form. The system prevents invalid inputs and provides clear error messages.

- **Invalid Email Example**  
  Form validation prevents registration with an invalid email address.  
  ![Registration error - email](docs/readme/registration-error-email.png)

- **Invalid Password Example**  
  Password validation ensures strong and matching passwords.  
  ![Registration error - password](docs/readme/registration-error-password.png)

- **Registration Form**  
  ![Registration form](docs/readme/registration-form.png)

- **Successful Registration**  
  Once registered, users are automatically logged in.  
  ![Registration success](docs/readme/register-success.png)

### Login & Logout

- **Login form** - Users can log in with their username or email and password. 
![Login form](docs/readme/login-form.png)

- **Login error** – if incorrect credentials are entered, a clear error message is displayed above the form.  
![Login Error Password](docs/readme/login-error-password.png)

- **Successful login** – users are redirected to the homepage.  
![Login Form](docs/readme/register-success.png)

- **Logout**  
  Users can safely log out from their account at any time, with the option to cancel.
![Confirm Logout](docs/readme/logout.png)
![Logout success](docs/readme/logout_success.png)



### Landing Page

The landing page changes depending on whether the user is logged in or logged out.

- **Logged Out View** – users are prompted to sign up to access more features.  
  ![Landing page logged out](docs/readme/landing-logged-out.png)

- **Logged In View** – authenticated users can browse recipes directly.  
  ![Landing page logged in](docs/readme/landing-logged-in.png)


### Recipe Detail Page

Each recipe has its own detail page where users can view the full instructions, ingredients, and reviews.  

- **Owner View**  
  When viewing their own recipe, users can edit or delete it.  
  ![Recipe detail owner](docs/readme/recipe-detail-owner.png)

- **Other User View**  
  Other users can favourite the recipe or leave a review.  
  ![Recipe detail user](docs/readme/recipe-detail-user.png)


### Add Recipe

Authenticated users can add their own recipes via a simple form. Validation prevents incomplete or invalid submissions.

- **Add Recipe Form**  
  ![Add recipe form](docs/readme/add-recipe-form.png)

- **Successful Creation**  
  After submitting, the user is redirected to the new recipe’s detail page with a success message.  
  ![Add recipe success](docs/readme/add-recipe-success.png)

### Edit Recipe

Recipe owners can update their recipes via the edit form. A success message confirms the changes.

- **Edit Recipe Form**  
  ![Edit recipe form](docs/readme/edit-recipe-form.png)

- **Successful Update**  
  After saving, the user is redirected to the recipe’s detail page with a success message.  
  ![Edit recipe success](docs/readme/edit-recipe-success.png)


### Delete Recipe

Only the recipe owner can delete a recipe. A confirmation step prevents accidental deletion.

- **Delete Confirmation**  
  ![Delete recipe confirmation](docs/readme/delete-recipe-confirm.png)

- **Successful Deletion**  
  After confirming, the user is redirected to the recipe list with a success message.  
  ![Delete recipe success](docs/readme/delete-recipe-success.png)



### **Future Features**
- Advanced filtering by cuisine, dietary needs, and cooking time.
- Rating system for recipes.
- Social sharing options.

---

## **Technologies Used**
- **HTML5**, **CSS3**, **JavaScript**
- **Python 3**, **Django** (with Class-Based and Function-Based Views)
- **PostgreSQL** for database
- **Bootstrap 5** for front-end styling
- **GitHub** for version control and project management
- **Heroku** for deployment
- **Crispy Forms** for form rendering
- **djrichtextfield** for rich text editing in recipes
- **Cloudinary** for media storage

---

## **Testing**

A summary of testing is included here, with full details available in [TESTING.md](TESTING.md).

### **User Story Testing**
The table below shows the testing outcome for each user story:

| User Story                                                                 | Test Result |
|----------------------------------------------------------------------------|-------------|
| As a user, I can register for an account so that I can create and manage my own recipes. | ✅ Pass |
| As a user, I can log in and log out so that I can access my account securely. | ✅ Pass |
| As a user, I can add a recipe so that I can share it with others. | ✅ Pass |
| As a user, I can edit my recipe so that I can update or correct it. | ✅ Pass |
| As a user, I can delete my recipe so that I can remove it if necessary. | ✅ Pass |
| As a user, I can browse recipes so that I can find cooking inspiration. | ✅ Pass |
| As a user, I can review recipes so that I can share my feedback. | ✅ Pass |
| As a user, I can mark recipes as favourites so that I can easily find them later. | ✅ Pass |
| As a user, I can search for recipes so that I can quickly find a recipe by keyword. | ✅ Pass |
| As a user, I can view my own recipes so that I can manage them in one place. | ✅ Pass |
| As a user, I can remove a recipe from my favourites list. | ✅ Pass |
| As a user, I can filter recipes by category so that I can find recipes by type. | Not Implemented |
| As a user, I can upload a profile picture to personalise my account. | Not Implemented |
| As a user, I can share recipes on social media. | Not Implemented |

---

### **HTML Validation**
All key pages were validated using the W3C Markup Validation Service, and passed with no errors.  
Full validation results and screenshots can be found in the [Testing Documentation](TESTING.md#html-validation).

---

## **Deployment**
The site was deployed to Heroku using the following steps:
1. Create a new Heroku app.
2. Connect the Heroku app to the GitHub repository.
3. Set environment variables in Heroku config vars.
4. Push final code to GitHub, triggering a Heroku build and deployment.

---

## **Credits**
- Recipe data: user-generated.
- Favicon: [favicon.io](https://favicon.io)
- Layout inspiration: Various cooking and recipe-sharing websites.

---