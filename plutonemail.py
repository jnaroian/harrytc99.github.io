from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Function to connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database'
    )

# Define your Flask routes here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email', methods=['POST'])
def submit_email():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                # Insert the email into the database
                cursor.execute("INSERT INTO emails (email) VALUES (%s)", (email,))
                conn.commit()
                cursor.close()
                conn.close()
                message = "Email submitted successfully!"
            except Exception as e:
                message = "An error occurred: " + str(e)
        else:
            message = "Email cannot be empty!"
        return render_template('message.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
