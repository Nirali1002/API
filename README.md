# API
 A FastAPI-based RESTful API with full CRUD operations, data validation using Pydantic, and interactive Swagger documentation. Ready for deployment on Render.
# 🚀 FastAPI CRUD API

Hurray! I'm happy to explore API development with **FastAPI**.  
This project is a fully functional, deployable RESTful API with:

- ✅ Full CRUD (Create, Read, Update, Delete)
- ✅ Data validation using **Pydantic**
- ✅ Auto-generated Swagger docs (`/docs`)
- ✅ Lightweight and beginner-friendly project structure
- ✅ Ready for free deployment on **Render**

---

## 🛠️ Technologies Used

- **FastAPI** – Python web framework for building APIs
- **Uvicorn** – ASGI server to run the app
- **Pydantic** – Data validation and schema generation

---

## 📦 Project Structure

# Example render.yaml content

services:
  - type: web
    name: fastapi-api
    runtime: python
    buildCommand: ""
    startCommand: uvicorn main:app --host 0.0.0.0 --port 10000
    envVars:
      - key: PYTHON_VERSION
        value: 3.11
    plan: free
