# Join (Backend)

## Description
The Join-Backend is a Django REST Framework (DRF) application for managing tasks and contacts. Create and organize tasks using drag and drop functions, assign users and categories.

---

## Tech Stack
- **Python**: 3.x
- **Django**: 5.1.4
- **Django REST Framework**: 3.15.2
- **CORS Headers**: 4.6.0
- **SQLParse**: 0.5.3
- **ASGIRef**: 3.8.1
- **Database**: SQLite 

---

## Installation

### Clone the Repository
```sh
git clone https://github.com/mariuskas1/join_backend.git
cd join_backend
```
### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```
### Install Dependencies
```sh
pip install -r requirements.txt
```
### Apply Migrations
```sh
python manage.py migrate
```
### Start the Development Server
```sh
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/

