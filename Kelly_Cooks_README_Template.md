
# Kelly Cooks

![Mockup Screenshots](docs/images/mockup-screenshots.png)

Kelly Cooks is an online app designed for food enthusiasts and home cooks to share and discover recipes. It enables users to interact through recipe sharing, saving favorites, and engaging in conversations about food.  

[The deployed website can be found here](https://your-deployment-link.com) _(Replace with your actual link)._

## Contents

1. [User Experience (UX)](#1-user-experience-ux)
2. [Agile Development](#2-agile-development)
3. [Design](#3-design)
4. [Features](#4-features)
5. [Technologies Used](#5-technologies-used)
6. [Local Development and Deployment](#6-local-development-and-deployment)
7. [Testing](#7-testing)
8. [Credits](#8-credits)

---

## 1. User Experience (UX)

### Target Audience
- Home cooks and food enthusiasts.
- Users interested in sharing or discovering recipes.

### User Goals
- Find, save, and share recipes easily.
- Interact with the community through recipe likes and comments.

### User Stories
_(Place user stories here. Add new ones as needed.)_
- Example: As a user, I want to save my favorite recipes so that I can access them easily later.

---

## 2. Agile Development

### Development Methodology
- Agile methodology with **GitHub** was used to track progress via Epics, User Stories, and Tasks.
- A **Kanban Board** was maintained for task prioritization.

![Kanban Board](docs/images/kanban.png) _(Replace with actual screenshot.)_

### Project Management Tools
- GitHub Issues
- ZenHub for tracking progress
- MoSCoW prioritization technique for User Stories

---

## 3. Design

### Wireframes
_(Insert your wireframe links/screenshots here.)_

- Example: [Home Page](docs/wireframes/home-page.png)

### Color Scheme
- Add details about the chosen color palette here.

### Typography
- Fonts used: `Roboto` for readability and `Reenie Beanie` for decorative purposes.

### Icons and Imagery
- Sourced from [Font Awesome](https://fontawesome.com) and [RawPixel](https://rawpixel.com).

---

## 4. Features

### Existing Features
_(Provide a high-level list of features. Replace placeholders.)_

- **Navigation Menu**: Easy-to-use and responsive across devices.
- **Recipe Management**: Users can create, edit, delete, and view recipes.
- **Favorites and Likes**: Users can save or like recipes to engage with content.
- **Authentication**: User account management with sign-up, log-in, and log-out functionality.

### Future Features
_(Add features you plan to develop in the future.)_
- Example: Advanced recipe search functionality.

---

## 5. Technologies Used

### Languages
- HTML5
- CSS3
- JavaScript
- Python

### Frameworks, Libraries, and Tools
- **Django** for backend development.
- **Bootstrap 5** for responsive design.
- **Cloudinary** for media storage.
- **Heroku** for deployment.

---

## 6. Local Development and Deployment

### Local Setup Instructions
1. Clone the repository:  
   ```bash
   git clone https://github.com/MaireadKelly/Kelly-Cook.git
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in an `env.py` file:  
   ```python
   import os

   os.environ["DATABASE_URL"] = "<your-database-url>"
   os.environ["SECRET_KEY"] = "<your-secret-key>"
   os.environ["CLOUDINARY_URL"] = "<your-cloudinary-url>"
   ```

4. Apply migrations and run the development server:  
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Deployment Instructions
_(Provide details about your deployment platform, e.g., Heroku, AWS.)_

---

## 7. Testing

### Manual Testing
_(Provide a brief outline of your testing approach.)_

### Automated Testing
- Unit tests written using Django’s built-in testing framework.
- Code coverage: 85% _(Replace with actual percentage)._

---

## 8. Credits

### Code
- Portions of code inspired by [Code Institute](https://codeinstitute.net) walkthroughs.
- External tutorials referenced for specific features like dynamic forms.

### Media
- Recipe images sourced from [RawPixel](https://rawpixel.com).

### Acknowledgments
- Special thanks to **Mentor Name** for guidance and feedback. _(Replace with actual name.)_
