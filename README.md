Recipe Sharing App



Recipe Sharing App is an online platform designed for food enthusiasts and home cooks to share recipes and join discussions. Users can browse published recipes, save favorites, and interact by commenting and liking. Registered users can submit their recipes for publication, edit, or delete them as needed. Admins review and approve recipes before publication.

The deployed website can be found here

Contents

User Experience (UX)

Agile Development

Design

Features

Technologies Used

Local Development and Deployment

Testing

Credits

1. User Experience (UX)

User Stories

Epic: Navigation

As a user, I can use a simple navigation menu to easily find content.

As a user, I can view the navigation menu on any screen size to ensure smooth navigation across devices.

Epic: Recipe CRUD

As a user, I can create recipes and request publication to share them with others.

As a user, I can edit or delete my recipes to manage my content.

As a user, I can like or save recipes to engage with content and keep a personal collection.

As an admin, I can approve or reject recipes to moderate site content.

Epic: User Account

As a user, I can register, log in, and log out securely to access features.

Target Audience

Food enthusiasts.

Home cooks.

Users interested in sharing and discovering recipes.

Goals

Build a community-driven platform for sharing recipes.

Provide an easy-to-navigate and interactive experience.

2. Agile Development

This project was developed using Agile methodologies with a Kanban board to track user stories and tasks.

Kanban Board Link

3. Design

Wireframes

Base Layout

Home Page

Recipe Detail Page

Color Scheme

Color palette sourced from Coolors.

Typography

Fonts from Google Fonts:

'Roboto' for a clean and readable appearance.

'Reenie Beanie' for decorative elements.

Imagery

Recipe and placeholder images sourced from BBC Good Food.

4. Features

Key Features

User Interaction:

Like, save, and comment on recipes.

Recipe Management:

Create, edit, and delete recipes.

Request publication for admin approval.

Admin Controls:

Moderate recipes and comments.

Approve or reject user submissions.

Future Features

Add user profiles.

Enhance search functionality.

5. Technologies Used

Languages

HTML5, CSS3, JavaScript, Python

Frameworks & Libraries

Django, Bootstrap, jQuery, Font Awesome

Tools

Heroku, Cloudinary, ElephantSQL, GitHub

6. Local Development and Deployment

Local Setup

Clone the repository:

git clone <repo-url>

Install dependencies:

pip install -r requirements.txt

Set up environment variables in env.py:

os.environ['SECRET_KEY'] = '<secret-key>'
os.environ['DATABASE_URL'] = '<database-url>'
os.environ['CLOUDINARY_URL'] = '<cloudinary-url>'

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Deployment

Hosted on Heroku with PostgreSQL and Cloudinary integration.

7. Testing

Manual Testing

Browser compatibility tested on Chrome, Firefox, and Edge.

Responsive design tested on mobile, tablet, and desktop devices.

Automated Testing

Django unit tests implemented.

[Placeholder for detailed testing section]

8. Credits

Content

Recipes sourced from BBC Good Food.

Tools

Coolors for color palettes.

Google Fonts for typography.

Acknowledgements

Special thanks to mentors and peers for guidance.

