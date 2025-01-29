# Testing Checklist

## Overview
This checklist covers manual and automated tests to ensure all functionalities of the Recipe Sharing App are working as intended. Print this document for tracking and recording test results during the testing phase.

---

## Table of Contents

1. [User Stories Testing](#user-stories-testing)
2. [Features Testing](#features-testing)
3. [Browser Compatibility](#browser-compatibility)
4. [Responsive Design Testing](#responsive-design-testing)
5. [Code Validation](#code-validation)
6. [Automated Testing](#automated-testing)
7. [Bug Tracking](#bug-tracking)
8. [Accessibility Testing](#accessibility-testing)
9. [Performance Testing](#performance-testing)

---

## User Stories Testing

| **User Story**                          | **Test**                                    | **Pass/Fail** | **Comments**                                    |
|-----------------------------------------|---------------------------------------------|---------------|-------------------------------------------------|
| Register for an account                 | Navigate to sign-up page and complete form  |               | Test invalid email formats, duplicate usernames |
| Log in to the app                       | Enter credentials on login page             |               | Test incorrect passwords, unregistered emails   |
| Add a recipe                            | Submit a recipe via the form                |               | Test with missing required fields               |
| Edit a recipe                           | Modify an existing recipe                   |               | Test simultaneous edits by multiple users       |
| Delete a recipe                         | Remove a recipe                             |               | Verify associated data is removed correctly     |
| Search for recipes                      | Use search bar to find recipes              |               | Test non-existent keywords, special characters  |
| Favorite a recipe                       | Mark a recipe as favorite                   |               | Check persistence of favorite state             |
| Follow another user                     | Navigate to a user profile and follow them  |               | Verify notifications or follow state            |

---

## Features Testing

### Navigation Bar
1. Verify all navigation links redirect to the correct pages.
2. Click on dropdown menus to ensure options are displayed correctly.
3. Take screenshots of dropdowns and their functionality.
4. Test for navigation bar responsiveness on different screen sizes.

### Footer
1. Ensure social media and contact links redirect appropriately.
2. Verify any clickable icons or text work as expected.
3. Confirm consistency across all pages.

### Recipe CRUD
1. Add a new recipe and verify it appears in the list.
2. Edit an existing recipe and confirm changes are reflected.
3. Delete a recipe and ensure it is removed from the database.
4. Verify that recipe deletion does not affect other users’ data.
5. Take screenshots for each step.

### Search Functionality
1. Enter various keywords into the search bar.
2. Verify results match the entered criteria.
3. Test with no results to ensure proper messaging.
4. Validate search functionality with special characters or long inputs.

### Login/Sign-Up Forms
1. Test validation by leaving fields empty or entering invalid data.
2. Verify error messages are displayed as expected.
3. Confirm successful login and sign-up redirect to the correct pages.
4. Test password reset and email verification workflows.

---

## Browser Compatibility

| **Browser**             | **Pass/Fail** | **Comments**            |
|--------------------------|---------------|-------------------------|
| Google Chrome (latest)   |               |                         |
| Mozilla Firefox (latest) |               |                         |
| Microsoft Edge           |               |                         |
| Safari                   |               |                         |
| Opera                    |               |                         |
| Brave                    |               |                         |
| Chrome v85               |               | Test compatibility with older versions      |

---

## Responsive Design Testing

| **Device**             | **Pass/Fail** | **Comments**            |
|-------------------------|---------------|-------------------------|
| Mobile (iPhone 12)      |               |                         |
| Tablet (iPad Pro)       |               |                         |
| Desktop (1920x1080)     |               |                         |
| Small Tablet (800x1280) |               |                         |
| Older Mobile (iPhone SE)|               |                         |

---

## Code Validation

| **Code**                | **Validation Tool**        | **Pass/Fail** | **Comments**            |
|--------------------------|----------------------------|---------------|-------------------------|
| HTML                    | W3C Validator              |               |                         |
| CSS                     | W3C CSS Validator          |               |                         |
| JavaScript              | ESLint                     |               |                         |
| Python                  | Pyflakes/Pylint            |               |                         |
| Tailwind/Bootstrap CSS  | Framework-specific tools   |               |                         |

---

## Automated Testing

| **Test**                | **Coverage** | **Pass/Fail** | **Comments**            |
|--------------------------|--------------|---------------|-------------------------|
| Models                  | 90%+         |               |                         |
| Views                   | 90%+         |               |                         |
| Forms                   | 90%+         |               |                         |
| End-to-End Tests        | 90%+         |               | Use Selenium or Cypress |

---

## Bug Tracking

| **Bug**                 | **Description**                             | **Fix Applied**          |
|--------------------------|---------------------------------------------|--------------------------|
| Example: Recipe not saving | Issue in form validation preventing save   | Adjusted validation rules |
|                          |                                             |                          |

---

## Accessibility Testing

1. Test keyboard navigation across all pages.
2. Validate ARIA roles and attributes.
3. Run automated tools like `axe` or Lighthouse for accessibility.
4. Verify screen reader compatibility (e.g., NVDA, JAWS).
5. Test color contrast ratios and font scalability.

---

## Performance Testing

1. Measure page load times using Lighthouse.
2. Test API response times and database query speeds.
3. Simulate heavy traffic loads using tools like Apache JMeter.
4. Check for caching of static files and optimized media delivery.

---

### Instructions
1. Print this checklist.
2. Perform tests and mark results in the **Pass/Fail** column.
3. Add comments for any observations or issues.
4. Attach screenshots for failures and log fixes in the Bug Tracking section.

---

**Prepared by:** [Your Name]  
**Date:** [Insert Date]
