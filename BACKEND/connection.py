from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host='database-1.cgl84qec82qv.us-east-1.rds.amazonaws.com',       
        user='admin',     
        password='123456789aA',
        database='test'
    )

@app.route('/getTable', methods=['GET'])
def get_tables():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()   # <-- estaba mal escrito (fectall)
        cursor.close()
        con.close()

        table_names = [table[0] for table in tables]
        return jsonify({"tables": table_names}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Connecting to DB...")
    app.run(debug=True, host="0.0.0.0")
