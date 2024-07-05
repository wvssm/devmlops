from flask import Flask
import os
import pymysql

app = Flask(__name__)

@app.route('/api/message')
def get_message():
    try:
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', 'db'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'password'),
            database=os.getenv('DB_NAME', 'myapp'),
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute("SELECT message FROM messages ORDER BY RAND() LIMIT 1")
            result = cursor.fetchone()
            return result['message'] if result else "No message found"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)