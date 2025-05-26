# FastAPI Social Media Backend

This is a **FastAPI** backend service for a social media application, providing CRUD operations, authentication, and feature toggles. The application is built with **FastAPI**, **PostgreSQL**, and **Python**, ensuring efficient database management and secure user authentication.

## Features
- 🚀 High-performance API using **FastAPI**
- 🔒 JWT-based authentication
- 📦 Database support with **SQLAlchemy & PostgreSQL**
- 🐳 Docker support for containerized deployment
- 🔄 Database version control and migrations using **Alembic**
- 📄 API documentation with Swagger UI (/docs) and ReDoc (/redoc)
---

## 1️ Installation

### Clone the Repository
```bash
git clone https://github.com/abhi1797/Backend-Social-media-app.git

```

### Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 2️ Environment Variables
Create a `.env` file with the following variables:
```ini
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
DATABASE_USERNAME=postgres
SECRET_KEY= #run secrets.token_hex(32) to generate a 64-character hex string (32 bytes)
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 3️ Running the Application

### Run FastAPI Locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Access API Documentation
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

##  Docker Deployment

### Build and Run Docker Container
```bash
docker-compose up -d   
```


## 4 Database Migrations

### Run Alembic Migrations
```bash
alembic upgrade head
```

### Create a New Migration
```bash
alembic revision --autogenerate -m "Describe migration"
```


## 5 API Endpoints

### Authentication
| Method | Endpoint       | Description         |
|--------|---------------|---------------------|
| `POST` | `/auth/login`  | Login with JWT     |
| `POST` | `/auth/signup` | Register a new user |

### Users
| Method | Endpoint       | Description         |
|--------|---------------|---------------------|
| `GET`  | `/users/`     | Get all users       |
| `POST` | `/users/`     | Create a new user   |

### Posts
| Method | Endpoint       | Description         |
|--------|---------------|---------------------|
| `GET`  | `/posts/`     | Get all posts       |
| `POST` | `/posts/`     | Create a new post   |
| `PUT`  | `/posts/{id}` | Update a post       |
| `DELETE` | `/posts/{id}` | Delete a post   |



## 6 Contributing
Feel free to submit pull requests or report issues.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your fork (`git push origin feature-branch`)
5. Create a Pull Request

- Testing the endpoints is still in progress , It will be uploaded as soon as i am done with the testing modules

## 🔹 Author
Developed by **Abhijit Sarkar**. Reach out at [abhijit.devops17@gmail.com].

