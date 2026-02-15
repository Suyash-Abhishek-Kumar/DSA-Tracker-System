import sqlite3
import random

def get_done_prerequisites(conn):
    c = conn.cursor()
    c.execute('SELECT topic, subtopic, number_of_questions, number_of_questions_done FROM dsa')
    topic_subs = {}
    for row in c.fetchall():
        topic, subtopic, num_q, num_done = row
        if num_q > 0:
            topic_subs.setdefault(topic, []).append(num_done == num_q)
    done_topics = set()
    for topic, completions in topic_subs.items():
        if all(completions):
            done_topics.add(topic)
    return done_topics

def get_eligible_questions(conn, done_topics):
    c = conn.cursor()
    c.execute('SELECT topic, subtopic, prerequisites, number_of_questions, number_of_questions_done FROM dsa')
    eligible = []
    for row in c.fetchall():
        topic, subtopic, prereq_str, num_q, num_done = row
        if num_done < num_q and num_q > 0:
            prereqs = [p.strip() for p in prereq_str.split(',') if p.strip()]
            if all(p in done_topics for p in prereqs):
                for i in range(num_done + 1, num_q + 1):
                    eligible.append((topic, subtopic, i))
    return eligible

def suggest_questions():
    conn = sqlite3.connect('dsa_topics.db')
    done_topics = get_done_prerequisites(conn)
    eligible = get_eligible_questions(conn, done_topics)
    conn.close()
    if not eligible:
        print("No eligible questions found.")
        return
    suggestions = random.sample(eligible, min(10, len(eligible)))
    for topic, subtopic, q_num in suggestions:
        print(f"{topic} - {subtopic} : Question #{q_num}")          # q_num refers to the nth unsolved question

if __name__ == "__main__":
    suggest_questions()
