from flask import Flask, render_template, request, redirect
import MySQLdb
import os

app = Flask(__name__)

# =========================
# Health Check Endpoint
# =========================
@app.route("/health")
def health():
    return "OK", 200


# =========================
# Database Configuration
# =========================
DB_HOST = os.getenv("DB_HOST", "mariadb-service")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USERNAME", "employee_user")
DB_PASS = os.getenv("DB_PASSWORD", "Emp@123456")
DB_NAME = os.getenv("DB_NAME", "employee_db")


def get_db_connection():
    return MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME,
        port=DB_PORT
    )


# =========================
# Home Page
# =========================
@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, department, email FROM employees ORDER BY id DESC"
    )
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", employees=employees)


# =========================
# Add Employee
# =========================
@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        name = request.form["name"]
        department = request.form["department"]
        email = request.form["email"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO employees (name, department, email) VALUES (%s, %s, %s)",
            (name, department, email)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/")

    return render_template("add_employee.html")


# =========================
# Delete Employee
# =========================
@app.route("/delete/<int:id>")
def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


# =========================
# Run Application
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
