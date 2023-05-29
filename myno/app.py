from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'words',
    # 'auth_plugin': 'mysql_native_password'
}

# API endpoint to get the word
@app.route('/api/word', methods=['GET'])
def get_word():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Retrieve the word from the database
        cursor.execute('SELECT word FROM word LIMIT 1')
        word = cursor.fetchone()[0]

        # Close the database connection
        cursor.close()
        conn.close()

        return jsonify({'word': word})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Admin portal endpoint to update the word
@app.route('/admin/update', methods=['POST'])
def update_word():
    try:
        new_word = request.json['word']

        # Connect to MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Update the word in the database
        cursor.execute('UPDATE word SET word = %s', (new_word,))
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Word updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
