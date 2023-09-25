# FastAPI cource practice

## Create virtual environment

python -m venv myvenv

## Activate virtual environment

- Windows: myvenv\Scripts\activate
- Linux: source myvenv/bin/activate

## Install libs & packeges

- python -m pip install --upgrade pip
- pip install -r requirements.txt

## Start app

- cd /src/
- uvicorn main:app --reload

## Docs are on the link

- http://localhost:8000/docs
- http://localhost:8000/redoc

## Put in JWT secret in .env

JWT_SECRET=your-secret
