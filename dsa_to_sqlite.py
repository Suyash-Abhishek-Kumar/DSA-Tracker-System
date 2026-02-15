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
                if topic_name == "Basics" or topic_name == "Sorting Techniques":
                    num_done = num_q
                elif topic_name == "Arrays":
                    num_done = 30
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

if __name__ == "__main__":
    conn, c = create_db()
    insert_data(conn, c, dsa_topics, topic_prerequisites)
    c.execute('UPDATE dsa SET prerequisites = "Basics, Arrays" WHERE topic = "Strings"')
    # desc_table(conn, c, "dsa")
    # select_all(conn, c, "dsa")
    conn.close()
