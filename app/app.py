from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)


def get_database_connection():
    return mysql.connector.connect(
        host="db",
        user="shopuser",
        password="shop_password",
        database="shopdb"
    )


def initialize_database():
    for attempt in range(10):
        try:
            connection = get_database_connection()
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    price DECIMAL(10,2)
                )
            """)

            cursor.execute("SELECT COUNT(*) FROM products")
            count = cursor.fetchone()[0]

            if count == 0:
                products = [
                    ("Laptop", 55000),
                    ("Smartphone", 25000),
                    ("Headphones", 2000),
                    ("Keyboard", 1500),
                    ("Mouse", 800)
                ]

                cursor.executemany(
                    "INSERT INTO products (name, price) VALUES (%s, %s)",
                    products
                )

                connection.commit()

            cursor.close()
            connection.close()

            print("Database initialized successfully.")
            return

        except mysql.connector.Error as error:
            print("Waiting for MySQL...", error)
            time.sleep(3)


@app.route("/")
def home():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", products=products)


if __name__ == "__main__":
    initialize_database()

    app.run(
        host="0.0.0.0",
        port=5000
    )