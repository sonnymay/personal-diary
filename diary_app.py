import sqlite3

def connect_db():
    connection = sqlite3.connect('diary.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);')
    connection.commit()
    return connection, cursor

def add_entry(connection, cursor, date, content):
    cursor.execute('INSERT INTO entries (content, date) VALUES (?, ?);', (content, date))
    connection.commit()

def view_all_entries(connection, cursor):
    cursor.execute('SELECT * FROM entries;')
    return cursor.fetchall()

def search_entry_by_date(cursor, date):
    cursor.execute("SELECT * FROM entries WHERE date = ?;", (date,))
    return cursor.fetchall()

def edit_entry(connection, cursor, id, new_content):
    cursor.execute('UPDATE entries SET content = ? WHERE id = ?;', (new_content, id))
    connection.commit()
               
def delete_entry(connection, cursor, id):
    cursor.execute('DELETE FROM entries WHERE id = ?;', (id,))
    connection.commit()

def main():
    conn, cur = connect_db()
    while True:
        print("1. Add new entry")
        print("2. View entries")
        print("3. Search entry by date")
        print("4. Edit entry")
        print("5. Delete entry")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date: (YYYY-MM-DD) ")
            content = input("Enter content: ")
            add_entry(conn, cur, date, content)
        elif choice == '2':
            entries = view_all_entries(conn, cur)
            for entry in entries:
                print(entry)
        elif choice == '3':
            date = input("Enter date to search: (YYYY-MM-DD) ")
            entries = search_entry_by_date(cur, date)
            for entry in entries:
                print(entry)
        elif choice == '4':
            id = input("Enter id of entry to edit: ")
            new_content = input("Enter new content: ")
            edit_entry(conn, cur, id, new_content)
        elif choice == '5':
            id = input("Enter id of entry to delete: ")
            delete_entry(conn, cur, id)
        elif choice == '6':
            conn.close()
            break

if __name__ == '__main__':
    main()

