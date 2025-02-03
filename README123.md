# Recipe Sharing App

![Mockup Screenshots](docs/images/mockup-screenshots.png)

Recipe Sharing App is an online platform designed for food enthusiasts and home cooks to share their favorite recipes. Users can browse through publicly available recipes, submit their own, and interact with the community by saving or commenting on recipes.

[Live Application](https://vjp-recipe-book-821f4ac9817f.herokuapp.com/)

## Table of Contents:
1. [User Experience (UX)](#user-experience-ux)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgments](#acknowledgments)

---

## **User Experience (UX)**

### **User Stories**
#### **Navigation**
- As a user, I want a simple navigation menu to find content easily.
- As a user, I want the navigation menu to be accessible on all devices.
- As a user, I want to see social media links for community interaction.

#### **Recipe CRUD Operations**
- As a registered user, I want to submit recipes.
- As a user, I want to edit or update my submitted recipes.
- As a user, I want to delete my own recipes.

---

## **Features**

### **Navigation Bar**
- Provides quick access to Home, Recipe List, Submit Recipe, and User Profile.
- Responsive on all screen sizes.

### **Recipe Submission**
- Users can submit new recipes using a structured form.
- Recipes include images, ingredients, and step-by-step instructions.

### **Recipe Viewing & Management**
- Recipes can be saved in "My Recipe Book."
- Users can edit or delete their recipes.

### **User Authentication**
- Secure user login and registration.

### **Admin Dashboard**
- Admins can add, edit or delete, Users, Recipes and Reviews

---

## **Technologies Used**
- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Hosting:** Heroku
- **Storage:** Cloudinary for image uploads

---

## **Libraries Used**
- Django
- Gunicorn
- Cloudinary
- dotenv
- SQLite

---

## **Testing**
- **Manual Testing:** Validated all user stories through structured tests.
- **Automated Testing:** Django test suite used for model and view testing.
- **Browser Compatibility:** Verified across Chrome, Firefox, Edge.
- **Code Validation:** Python (PEP8), HTML, CSS validation performed.

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
- Code snippets from Django documentation.
- Icons and images sourced from Unsplash and FontAwesome.

---

## **Acknowledgments**
Special thanks to my mentor and colleagues for their guidance.
