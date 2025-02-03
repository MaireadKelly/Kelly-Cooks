# Testing Documentation

This document outlines the testing process and results for the Recipe Sharing App.

## **Table of Contents**
1. [Manual Testing](#manual-testing)
2. [Automated Testing](#automated-testing)
3. [Browser Compatibility](#browser-compatibility)
4. [Responsiveness](#responsiveness)
5. [Code Validation](#code-validation)
6. [Bugs](#bugs)

---

## **Manual Testing**
### **User Stories**
| User Story | Test Steps | Status |
|------------|------------|--------|
| Navigate website easily | Load website and use menu navigation | ✅ |
| Submit new recipe | Fill and submit recipe form | ✅ |
| Edit recipe | Open recipe and edit details | ✅ |
| Delete recipe | Remove recipe from profile | ✅ |

### **Features Testing**
| Feature | Expected Result | Status |
|---------|---------------|--------|
| Login | User logs in successfully | ✅ |
| Logout | User logs out successfully | ✅ |
| Recipe submission | Recipe appears in dashboard | ✅ |

---

## **Automated Testing**
Django's built-in testing framework was used to validate:
- Model integrity
- View responses
- Form validation

Tests were run using:
```sh
python manage.py test
