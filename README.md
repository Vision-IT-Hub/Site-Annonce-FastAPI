# Site-Annonce-FastAPI

## Старт

#### 1) Create  and activate virtualenv
    python -m venv venv
  
#### 2) Install requirements:
    pip install -r requirements.txt
    pip install 'fastapi-jwt-auth[asymmetric]'
    pip install "passlib[bcrypt]"

#### 3) Run migration
```bash
$ alembic init alembic
```
```bash
$ alembic revision --autogenerate -m "Migration Tables"
```

#### 4) generate RSA Keys in settings/credentials folder
```bash
$ openssl genrsa -out private.pem 4096
```
```bash
$ openssl rsa -in private.pem -pubout > public.pem
```

#### 5) Run server
```bash
$ uvicorn main:app --reload
```

### Documentation Redoc:
> http://127.0.0.1:8000/api/redoc |doc
