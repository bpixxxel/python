import sqlite3

def setup_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    ''')
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'alice', 'alicepass')")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (2, 'bob', 'bobpass')")
    conn.commit()
    conn.close()

def safe_query(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    result = cursor.fetchall()
    conn.close()
    return result

def unsafe_query(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def main():
    setup_database()
    while True:
        username = input("Enter username to search (or type 'exit' to quit): ")
        if username.lower() == 'exit':
            break
        method = input("Choose query type - Safe or Unsafe (S/U): ")
        if method.lower() == 's':
            results = safe_query(username)
            print("Safe Query Results:", results)
        elif method.lower() == 'u':
            results = unsafe_query(username)
            print("Unsafe Query Results:", results)
        else:
            print("Invalid choice. Please enter 'S' for Safe or 'U' for Unsafe.")

if __name__ == "__main__":
    main()
