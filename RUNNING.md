# How to Run the Project

This project consists of a Flask Backend and a Flask Frontend.

## Prerequisites

- Python 3.x installed
- pip installed

## 1. Install Dependencies

### Backend
Open a terminal in the project root and run:
```bash
pip install -r BACKEND/requirements.txt
```

### Frontend
The frontend requires `Flask` and `requests`. Run:
```bash
pip install Flask requests
```

## 2. Run the Application

You need to run the backend and frontend in separate terminals.

### Step 1: Start the Backend
Open a terminal in the project root and run:
```bash
python BACKEND/app.py
```
The backend will start on `http://127.0.0.1:5000`.
It will automatically attempt to connect to the configured MySQL database.

### Step 2: Start the Frontend
Open a NEW terminal in the project root and run:
```bash
python FRONTEND/app.py
```
The frontend will start on `http://127.0.0.1:3000`.

## 3. Access the Application

Open your browser and go to:
[http://127.0.0.1:3000](http://127.0.0.1:3000)

You should see the application interface.
