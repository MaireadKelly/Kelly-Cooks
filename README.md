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