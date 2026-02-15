# DSA Tracker System

A prerequisite-driven Data Structures & Algorithms (DSA) practice tracker that recommends problems based on concept dependencies and tracks learning progress using a SQLite database.

This project models DSA topic relationships, tracks completion status, and suggests eligible questions based on prerequisite satisfaction to support structured and efficient problem solving.

---

## Overview

The DSA Tracker System helps users practice DSA systematically by enforcing topic prerequisites and recommending questions only from topics they are prepared for.

Instead of solving problems randomly or repeatedly practicing a single topic, the system introduces controlled randomness while maintaining a structured learning path.

---

## Features

- **Prerequisite-based learning**
  - Models dependencies between DSA topics
  - Unlocks topics only when prerequisites are completed

- **Progress tracking**
  - Stores topic and subtopic progress using SQLite
  - Tracks number of questions completed per topic

- **Question suggestion engine**
  - Recommends eligible unsolved questions
  - Randomized selection for practice variety

- **Structured DSA dataset**
  - Organized topic → subtopic → question count mapping
  - Configurable prerequisite relationships

- **Local database storage**
  - Lightweight SQLite backend
  - Persistent progress tracking

---

## Project Structure

```
.
├── data.py                # DSA topics and prerequisite mappings
├── dsa_to_sqlite.py      # Database creation and data insertion
├── suggest_questions.py  # Question recommendation engine
├── dsa_topics.db         # SQLite database (generated locally)
```

---

## How It Works

1. DSA topics and prerequisites are defined in `data.py`.
2. Topic data is stored in a SQLite database.
3. The system checks completed topics.
4. Only questions from eligible topics are suggested.
5. Users progress by completing questions and unlocking new topics.

---

## Setup & Usage

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/DSA-Tracker-System.git
cd DSA-Tracker-System
```

---

### 2. Create and populate database

```
python dsa_to_sqlite.py
```

This creates the SQLite database and initializes topic data.

---

### 3. Get practice question suggestions

```
python suggest_questions.py
```

The system outputs eligible questions based on completed prerequisites.

---

## Example Output

```
Arrays - Medium : Question #5
Binary Search - BS on 1D Arrays : Question #2
Recursion - Subsequences Pattern : Question #3
...
```

---

## Tech Stack

- Python
- SQLite
- Pandas (for table inspection)
- Rule-based recommendation logic

---

## Motivation

While practicing DSA, repeatedly solving problems from the same topic for long periods can become monotonous and inefficient. This project was built to introduce controlled randomness into practice by suggesting problems from different topics while ensuring that prerequisite concepts are not skipped.

The goal is to balance variety and structure — allowing diverse problem practice without breaking the logical learning sequence required to understand advanced topics.

---

## Current Status

Work in progress.

Planned improvements:

- Automatic problem scraping from DSA sheets
- Better progress analytics
- API integration for question datasets

---

## License

Free to use for learning and personal development.
