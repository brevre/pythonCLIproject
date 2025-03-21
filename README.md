# pythonCLIproject
# **Library Management System (CLI + SQLAlchemy ORM)**  

## **Project Description**  
This is a **Command-Line Interface (CLI) Library Management System** that allows users to:  
- **Register as a library member**  
- **Add books** to the library  
- **Borrow and return books**  
- **View available books and members**  

It uses **Python, SQLAlchemy ORM, and Alembic** for database management.  

---

## **Technologies Used**  
- **Python 3.x**  
- **Click** (for CLI interactions)  
- **SQLAlchemy** (ORM for database)  
- **Alembic** (for database migrations)  
- **Pipenv** (for virtual environment management)  

---

## **Setup Instructions**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/library-cli-project.git
cd library-cli-project
```

### **2️⃣ Set Up Virtual Environment**  
```bash
pipenv install
pipenv shell
```

### **3️⃣ Initialize the Database**  
Run Alembic migrations to create the database:  
```bash
alembic upgrade head
```

---

## **How to Use the CLI**  

### **1️⃣ Register a New User**  
```bash
python cli.py register "Alice" "alice@example.com"
```

### **2️⃣ Add a New Book**  
```bash
python cli.py addbook "1984" "George Orwell"
```

### **3️⃣ View Available Books**  
```bash
python cli.py books
```

### **4️⃣ Borrow a Book**  
```bash
python cli.py borrow 1 1
```
_(Where `1 1` is `user_id` and `book_id`.)_

### **5️⃣ Return a Book**  
```bash
python cli.py returnbook 1
```
_(Where `1` is `book_id`.)_

---

## **Project Structure**  
```
library-cli-project/
│── alembic/              # Alembic migrations folder  
│── models.py             # Database models  
│── database.py           # Database connection setup  
│── cli.py                # Command-line interface logic  
│── crud.py               # CRUD operations for database  
│── Pipfile               # Pipenv dependencies  
│── README.md             # Project documentation  
```

---

## **Future Improvements**  
- Add **authentication for users**  
- Implement **book reservation feature**  
- Add **due dates and penalties for late returns**  

---
