import sqlite3
import ast
from data import dsa_topics, topic_prerequisites
import pandas

# Create SQLite database and table
def create_db():
    conn = sqlite3.connect('dsa_topics.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS dsa (
            topic TEXT,
            subtopic TEXT,
            prerequisites TEXT,
            number_of_questions INTEGER,
            number_of_questions_done INTEGER
        )
    ''')
    conn.commit()
    return conn, c

def desc_table(conn, c, table):
    # SQLite uses PRAGMA table_info instead of DESC
    # Cannot use ? for table names, but validate the input
    if not table.replace('_', '').isalnum():
        raise ValueError("Invalid table name")
    
    c.execute(f'PRAGMA table_info({table})')
    columns = c.fetchall()
    
    # Print in a readable format
    print(f"\nTable: {table}")
    print("-" * 80)
    print(f"{'ID':<5} {'Name':<30} {'Type':<15} {'NotNull':<10} {'Default':<10} {'PK':<5}")
    print("-" * 80)
    for col in columns:
        print(f"{col[0]:<5} {col[1]:<30} {col[2]:<15} {col[3]:<10} {str(col[4]):<10} {col[5]:<5}")
    print("-" * 80)
    
    return columns

def select_all(conn, c, table):
    """Display all rows from a table"""
    # Validate table name to prevent SQL injection
    if not table.replace('_', '').isalnum():
        raise ValueError("Invalid table name")
    
    # Get column names first
    c.execute(f'PRAGMA table_info({table})')
    columns = c.fetchall()
    col_names = [col[1] for col in columns]
    
    # Get all rows
    c.execute(f'SELECT * FROM {table}')
    rows = c.fetchall()
    pandas.set_option('display.max_rows', None)
    df = pandas.DataFrame(rows)
    print(df)

# Insert data into the database
def insert_data(conn, c, dsa_topics, prerequisites):
    for topic, subtopics in dsa_topics.items():
        topic_name = topic.split('[')[0].strip()
        prereq = prerequisites.get(topic_name, [])
        prereq_str = ', '.join(prereq)
        if isinstance(subtopics, dict):
            for subtopic, num_q in subtopics.items():
                if topic_name == "Basics" or topic_name == "Sorting Techniques" or (topic_name == "Arrays" and subtopic != "Hard"):
                    num_done = num_q
                elif topic_name == "Arrays" and subtopic == "Hard":
                    num_done = 2
                else:
                    num_done = 0
                c.execute('INSERT INTO dsa VALUES (?, ?, ?, ?, ?)',
                          (topic_name, subtopic, prereq_str, num_q, num_done))
        else:
            # If no subtopics, treat topic as subtopic
            num_q = subtopics if isinstance(subtopics, int) else 0
            if topic_name == "Basics" or topic_name == "Sorting Techniques":
                num_done = num_q
            elif topic_name == "Arrays":
                num_done = 30
            else:
                num_done = 0
            c.execute('INSERT INTO dsa VALUES (?, ?, ?, ?, ?)',
                      (topic_name, topic_name, prereq_str, num_q, num_done))
    conn.commit()

def update_status(conn, c):
    """Update question completion status from a CSV file"""
    try:
        print(1)
        csv_file = "curr_doing.csv"
        df = pandas.read_csv(csv_file)
        print(2)
        print(df)
        # Assuming CSV has 'topic' and 'subtopic' columns
        for _, row in df.iterrows():
            print("2." + str(_))
            topic = row['topic']
            subtopic = row['subtopic']
            c.execute('''UPDATE dsa SET number_of_questions_done = number_of_questions_done + 1 
                         WHERE topic = ? AND subtopic = ?''', (topic, subtopic))
        print(3)
        conn.commit()
        print(f"Updated {c.rowcount} records successfully.")

    except FileNotFoundError:
        print("CSV file not found.")
    except KeyError as e:
        print(f"CSV column not found: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    conn, c = create_db()
    # insert_data(conn, c, dsa_topics, topic_prerequisites)
    # conn.commit()

    while True:
        print("\n" + "="*50)
        print("DSA Trainer Menu")
        print("="*50)
        print("1. View table structure")
        print("2. View all topics")
        print("3. Update question status from CSV")
        print("4. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            desc_table(conn, c, "dsa")
        elif choice == "2":
            select_all(conn, c, "dsa")
        elif choice == "3":
            update_status(conn, c)
        elif choice == "4":
            print("Exiting...")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")
