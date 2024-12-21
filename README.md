
# AI Video Script Generator

## Overview
This web application allows users to generate AI-powered video scripts by utilizing the `x.ai` API. 
Users can provide prompts, upload files, and add external links to enhance the AI prompt.

## Features
### Backend:
- Built with Django.
- Integrates `x.ai` API to generate scripts.
- Handles text inputs, file uploads, and link metadata extraction.
- Saves and retrieves user-generated scripts.

### Frontend:
- Built using HTML, TailwindCSS, and JavaScript.
- Dynamic input field supporting:
  - Text input for prompts.
  - File uploads (e.g., `.txt`, `.pdf`).
  - External links for metadata fetching.
- Displays AI-generated scripts dynamically.
- Fully responsive design.

---

## Directory Structure

### Backend:
```
backend/
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── scripts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
|   ├── openai_client.py
├── manage.py
├── requirements.txt
```

#### Key Files:
1. **`settings.py`**: Configures installed apps, media/static file settings, and other Django settings.
2. **`urls.py`**: Routes API endpoints and admin URLs.
3. **`models.py`**: Defines database models for scripts and uploaded files.
4. **`serializers.py`**: Serializes data for API responses.
5. **`views.py`**: Contains logic for handling requests and integrating with the `x.ai` API.
6. **`requirements.txt`**: Lists all dependencies for the backend.

### Frontend:
```
frontend/
├── index.html
├── scripts.js
├── tailwind.css
├── tailwind.config.js
```

#### Key Files:
1. **`index.html`**: Main HTML file containing the application layout and input fields.
2. **`scripts.js`**: Handles frontend interactivity and API calls.
3. **`tailwind.css`**: Includes TailwindCSS styles for responsive design.
4. **`tailwind.config.js`**: Configures TailwindCSS.

---

## Setup Instructions

### Backend Setup:
1. Install dependencies:
   ```bash
   pip install django djangorestframework requests PyPDF2
   ```
2. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
3. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup:
1. Install TailwindCSS dependencies:
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init
   ```
2. Configure `tailwind.config.js` to include `index.html` and `scripts.js` in the `content` array.
3. Serve the frontend using a static server or integrate it with Django’s `STATICFILES_DIRS`.

---

## How to Use the Application
1. Navigate to the application URL (default: `http://127.0.0.1:8000/`).
2. Enter a prompt in the input field, upload a file, or add a link.
3. Click the "Generate Script" button to fetch the AI-generated script.
4. View the generated script dynamically displayed below the input field.

---

## Dependencies
### Backend:
- Django
- Django REST Framework
- Requests
- PyPDF2

### Frontend:
- TailwindCSS
- JavaScript

---

## Limitations and Future Enhancements
### Current Limitations:
- Basic file and link handling.
- Limited to English for script generation.

### Future Enhancements:
- Add multi-language support.
- Enable downloading scripts as `.txt` or `.pdf`.
- Implement pagination and search for saved scripts.
- Add interactive file parsing.

---

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes with a detailed message.
4. Create a pull request for review.

---

## License
This project is open-source and available under the MIT License.
