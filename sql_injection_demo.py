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

def unsafe_query(query):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    print("Executing SQL query:", query)  # Debug output to see the constructed query
    try:
        cursor.execute(query)
        if cursor.description:  # Check if there are results to fetch
            result = cursor.fetchall()
            print("Query Results:", result)
        else:
            conn.commit()
            print("Query executed successfully.")
    except Exception as e:
        print("Error during SQL execution:", str(e))
    finally:
        conn.close()

def main():
    setup_database()
    while True:
        print("\nChoose an option:")
        print("1. Safe Query")
        print("2. Unsafe Query")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '3':
            break
        elif choice in ['1', '2']:
            if choice == '1':
                username = input("Enter username to search safely: ")
                results = safe_query(username)
                print("Safe Query Results:", results)
            elif choice == '2':
                query = input("Enter your SQL query (unsafe): ")
                unsafe_query(query)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
