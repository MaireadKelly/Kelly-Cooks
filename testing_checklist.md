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

---

## User Stories Testing

| **User Story**                          | **Test**                                      | **Pass/Fail** | **Comments**            |
|-----------------------------------------|----------------------------------------------|---------------|-------------------------|
| Register for an account                 | Navigate to sign-up page and complete form   |               |                         |
| Log in to the app                       | Enter credentials on login page             |               |                         |
| Add a recipe                            | Submit a recipe via the form                |               |                         |
| Edit a recipe                           | Modify an existing recipe                   |               |                         |
| Delete a recipe                         | Remove a recipe                              |               |                         |
| Search for recipes                      | Use search bar to find recipes              |               |                         |
| Favorite a recipe                       | Mark a recipe as favorite                   |               |                         |
| Follow another user                     | Navigate to a user profile and follow them  |               |                         |

---

## Features Testing

### Navigation Bar
1. Verify all navigation links redirect to the correct pages.
2. Click on dropdown menus to ensure options are displayed correctly.
3. Take screenshots of dropdowns and their functionality.

### Footer
1. Ensure social media and contact links redirect appropriately.
2. Verify any clickable icons or text work as expected.
3. Confirm consistency across all pages.

### Recipe CRUD
1. Add a new recipe and verify it appears in the list.
2. Edit an existing recipe and confirm changes are reflected.
3. Delete a recipe and ensure it is removed from the database.
4. Take screenshots for each step.

### Search Functionality
1. Enter various keywords into the search bar.
2. Verify results match the entered criteria.
3. Test with no results to ensure proper messaging.

### Login/Sign-Up Forms
1. Test validation by leaving fields empty or entering invalid data.
2. Verify error messages are displayed as expected.
3. Confirm successful login and sign-up redirect to the correct pages.

---

## Browser Compatibility

| **Browser**             | **Pass/Fail** | **Comments**            |
|--------------------------|---------------|-------------------------|
| Google Chrome            |               |                         |
| Mozilla Firefox          |               |                         |
| Microsoft Edge           |               |                         |
| Safari                   |               |                         |

---

## Responsive Design Testing

| **Device**             | **Pass/Fail** | **Comments**            |
|-------------------------|---------------|-------------------------|
| Mobile (iPhone 12)      |               |                         |
| Tablet (iPad Pro)       |               |                         |
| Desktop (1920x1080)     |               |                         |

---

## Code Validation

| **Code**                | **Validation Tool**        | **Pass/Fail** | **Comments**            |
|--------------------------|----------------------------|---------------|-------------------------|
| HTML                    | W3C Validator              |               |                         |
| CSS                     | W3C CSS Validator          |               |                         |
| JavaScript              | ESLint                     |               |                         |
| Python                  | Pyflakes/Pylint            |               |                         |

---

## Automated Testing

| **Test**                | **Coverage** | **Pass/Fail** | **Comments**            |
|--------------------------|--------------|---------------|-------------------------|
| Models                  | 90%+         |               |                         |
| Views                   | 90%+         |               |                         |
| Forms                   | 90%+         |               |                         |

---

## Bug Tracking

| **Bug**                 | **Description**                             | **Fix Applied**          |
|--------------------------|---------------------------------------------|--------------------------|
| Example: Recipe not saving | Issue in form validation preventing save   | Adjusted validation rules |

---

### Instructions
1. Print this checklist.
2. Perform tests and mark results in the **Pass/Fail** column.
3. Add comments for any observations or issues.
4. Attach screenshots for failures and log fixes in the Bug Tracking section.

---

**Prepared by:** [Your Name]  
**Date:** [Insert Date]

