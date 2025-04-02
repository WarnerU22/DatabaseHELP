import sqlite3

database_name = "sampleDB.db"

try:
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if tables:
        for table_name_tuple in tables:
            table_name = table_name_tuple[0]  # Extract table name

            print(f"Data in table: {table_name}")

            try:
                cursor.execute(f"SELECT * FROM {table_name}") #select all data
                rows = cursor.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("  (Table is empty)")

            except sqlite3.Error as e:
                print(f"  Error reading table {table_name}: {e}")

    else:
        print("No tables found.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if 'connection' in locals() and connection:
        cursor.close()