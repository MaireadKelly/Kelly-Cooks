# Kelly Cooks – Testing Documentation

This file contains full details of the testing carried out on the **Kelly Cooks** project.

---

## **HTML Validation**

All key pages were validated using the [W3C Markup Validation Service](https://validator.w3.org/).  
The following table summarises results:

| Page                             | URL Example                 | Result |
|----------------------------------|-----------------------------|--------|
| Landing Page                     | `/`                         | ✅ Pass |
| Recipe List                      | `/recipes/`                 | ✅ Pass |
| Recipe Detail                    | `/recipes/<id>/`            | ✅ Pass |
| Add Recipe                       | `/recipes/add/`             | ✅ Pass |
| Edit Recipe                      | `/recipes/edit/<id>/`       | ✅ Pass |
| Delete Confirmation              | `/recipes/delete/<id>/`     | ✅ Pass |
| My Recipes                       | `/recipes/my-recipes/`      | ✅ Pass |
| Favourites                       | `/recipes/favourites/`      | ✅ Pass |
| Add Review                       | `/recipes/<id>/review/`     | ✅ Pass |

### **Screenshots**
Screenshots of validation results are stored in:
- `docs/validation/landing-page-validation.png`
- `docs/validation/recipe-list-validation.png`
- `docs/validation/recipe-detail-validation.png`
- `docs/validation/add-recipe-validation.png`
- `docs/validation/edit-recipe-validation.png`
- `docs/validation/delete-recipe-validation.png`
- `docs/validation/my-recipes-validation.png`
- `docs/validation/favourites-validation.png`
- `docs/validation/add-review-validation.png`

---

## **CSS Validation**

CSS was validated using the [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/).  
Result: ✅ Pass with no errors.

Screenshot: `docs/validation/css-validation.png`

---

## **Python Validation**

Python code was checked with [PEP8 online validator](http://pep8online.com/).  
All files passed with no significant errors. Minor line length warnings remain in some files but are within acceptable limits.

Screenshot: `docs/validation/python-validation.png`

---

## **Lighthouse Testing**

Performance and accessibility were tested using Google Chrome DevTools Lighthouse audit.

### **Desktop**
![Lighthouse Desktop](docs/testing/lighthouse-desktop.png)

### **Mobile**
![Lighthouse Mobile](docs/testing/lighthouse-mobile.png)

**Note:** Best Practices improved after enforcing HTTPS for Cloudinary assets (`cloudinary.config(secure=True)` and `CLOUDINARY_SECURE=True`). Mixed-content warnings were re-tested and no longer appear.

---

## **Browser Compatibility**

The site was tested on the latest versions of:
- Google Chrome  
- Mozilla Firefox  
- Microsoft Edge  
- Safari (Mac/iOS)  

Screenshots:
- `docs/testing/browser-chrome.png`
- `docs/testing/browser-firefox.png`
- `docs/testing/browser-edge.png`
- `docs/testing/browser-safari.png`

---

## **Manual Feature Tests**

### **Authentication**
| Scenario | Steps | Expected | Result |
|---|---|---|---|
| Register new account | Visit Sign Up → submit valid details | Account created, user logged in | ✅ |
| Register invalid email | Submit invalid email | Inline error shown, no account created | ✅ |
| Login success | Visit Login → submit valid credentials | Logged in with success message | ✅ |
| Login failure | Submit wrong password | Error message above the form | ✅ |
| Logout | Click Logout | Session cleared, success message | ✅ |

### **CRUD – Recipes**
| Scenario | Steps | Expected | Result |
|---|---|---|---|
| Create recipe | Add Recipe → submit valid form | Redirect to recipe detail with success message | ✅ |
| Edit own recipe | Detail → Edit → submit | Redirect to detail with success message | ✅ |
| Cancel edit | Detail → Edit → **Cancel** | Return to detail, no changes | ✅ |
| Delete own recipe | Detail → Delete → confirm | Redirect to list with success message | ✅ |

### **Defensive Design (Permissions)**
| Scenario | Steps | Expected | Result |
|---|---|---|---|
| Non-owner: edit | Login as other user → visit `/recipes/edit/<id>/` | Error message, redirect to recipe detail (no 403 page) | ✅ |
| Non-owner: delete | Login as other user → visit `/recipes/delete/<id>/` | Error message, redirect to recipe detail (no debug page) | ✅ |

### **Reviews**
| Scenario | Steps | Expected | Result |
|---|---|---|---|
| Add review | Detail → Add Review → submit | Redirect to detail with success message; review visible | ✅ |
| Edit own review | On own review → Edit → submit | Redirect to detail with success message | ✅ |
| Delete own review | On own review → Delete | Redirect to detail with success message; review removed | ✅ |

### **Favourites & Lists**
| Scenario | Steps | Expected | Result |
|---|---|---|---|
| Toggle favourite on | Detail → “Add to favourites” | Success message; item appears in `/recipes/favourites/` | ✅ |
| Toggle favourite off | Detail → “Remove from favourites” | Success message; item removed from favourites | ✅ |
| My Recipes | Visit `/recipes/my-recipes/` | Only the user’s recipes are listed | ✅ |

---

## **User Story Testing**

> This table mirrors the README and includes **MoSCoW priorities**. Full evidence and screenshots are provided above.

| MoSCoW Priority | User Story                                                                 | Test Result |
|-----------------|-----------------------------------------------------------------------------|-------------|
| **Must Have**   | As a user, I can register for an account so that I can create and manage my own recipes. | ✅ Pass |
| **Must Have**   | As a user, I can log in and log out so that I can access my account securely. | ✅ Pass |
| **Must Have**   | As a user, I can add a recipe so that I can share it with others. | ✅ Pass |
| **Must Have**   | As a user, I can edit my recipe so that I can update or correct it. | ✅ Pass |
| **Must Have**   | As a user, I can delete my recipe so that I can remove it if necessary. | ✅ Pass |
| **Must Have**   | As a user, I can browse recipes so that I can find cooking inspiration. | ✅ Pass |
| **Must Have**   | As a user, I can review recipes so that I can share my feedback. | ✅ Pass |
| **Must Have**   | As a user, I can mark recipes as favourites so that I can easily find them later. | ✅ Pass |
| **Should Have** | As a user, I can search for recipes so that I can quickly find a recipe by keyword. | ✅ Pass |
| **Should Have** | As a user, I can view my own recipes so that I can manage them in one place. | ✅ Pass |
| **Should Have** | As a user, I can remove a recipe from my favourites list. | ✅ Pass |
| **Could Have**  | As a user, I can filter recipes by category so that I can find recipes by type. | Not Implemented |
| **Could Have**  | As a user, I can upload a profile picture to personalise my account. | Not Implemented |
| **Could Have**  | As a user, I can share recipes on social media. | Not Implemented |

---

## **Bugs & Fixes**

- **Edit Recipe “Cancel” loop** – Cancel now returns to **detail** (was looping back to edit).  
- **Delete Recipe debug page** – Non-owners are redirected with an error message (no 403/debug); owners see success + redirect.  
- **Favourites clarity** – Toggling favourites shows a success message; items appear/remove in **My Favourites**.  
- **Static files paths** – Corrected in `base.html` to load favicon and CSS correctly.  
- **Mixed content (Lighthouse)** – Enforced HTTPS for Cloudinary (`cloudinary.config(secure=True)`, `CLOUDINARY_SECURE=True`).

---

## **Conclusion**

All functional and non-functional requirements were met.  
Full validation evidence and screenshots are stored in `docs/validation/` and `docs/testing/`.

