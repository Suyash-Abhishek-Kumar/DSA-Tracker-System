import sqlite3
import ast

dsa_topics = {
    "Basics": {
        "Things to Know in C++/Java/Python or any language": 9,
        "Build-up Logical Thinking": 1,
        "Learn STL/Java-Collections or similar thing in your language": 2,
        "Know Basic Maths": 7,
        "Learn Basic Recursion": 9,
        "Learn Basic Hashing": 3
    },
    "Sorting Techniques": {
        "Sorting I": 3,
        "Sorting II": 4
    },
    "Arrays": {
        "Easy": 14,
        "Medium": 14,
        "Hard": 2
    },
    "Binary Search": {
        "BS on 1D Arrays": 13,
        "BS on Answers": 14,
        "BS on 2D Arrays": 5
    },
    "Strings [Basic and Medium, Strings]": {
        "Basic and Easy String Problems": 7,
        "Medium String Problems": 8
    },
    "Linked List": {
        "Learn 1D LinkedList": 5,
        "Learn Doubly LinkedList": 4,
        "Medium Problems of LL": 15,
        "Medium Problems of DLL": 3,
        "Hard Problems of LL": 4
    },
    "Recursion": {
        "Get a Strong Hold": 5,
        "Subsequences Pattern": 12,
        "Trying out all Combos / Hard": 8
    },
    "Bit Manipulation": {
        "Learn Bit Manipulation": 8,
        "Interview Problems": 5,
        "Advanced Maths": 5
    },
    "Stack and Queues": {
        "Learning": 8,
        "Prefix, Infix, PostFix Conversion Problems": 6,
        "Monotonic Stack/Queue Problems [VVV. Imp]": 11,
        "Implementation Problems": 5
    },
    "Sliding Window & Two Pointer": {
        "Medium Problems": 8,
        "Hard Problems": 4
    },
    "Heaps": {
        "Learning": 4,
        "Medium Problems": 7,
        "Hard Problems": 6
    },
    "Greedy Algorithms": {
        "Easy Problems": 5,
        "Medium/Hard": 11
    },
    "Binary Trees": {
        "Traversals": 13,
        "Medium Problems": 12,
        "Hard Problems": 14
    },
    "Binary Search Trees": {
        "Concepts": 3,
        "Practice Problems": 13
    },
    "Graphs": {
        "Learning": 6,
        "Problems on BFS/DFS": 14,
        "Topo Sort and Problems": 7,
        "Shortest Path Algorithms and Problems": 13,
        "MinimumSpanningTree/Disjoint Set and Problems": 10,
        "Other Algorithms": 3
    },
    "Dynamic Programming": {
        "Introduction to DP": 1,
        "1D DP": 5,
        "2D/3D DP and DP on Grids": 7,
        "DP on Subsequences": 11,
        "DP on Strings": 10,
        "DP on Stocks": 6,
        "DP on LIS": 7,
        "MCM DP | Partition DP": 7,
        "DP on Squares": 2
    },
    "Tries": {
        "Theory": 1,
        "Problems": 6
    },
    "String": {
        "Hard Problems": 9
    }
}

topic_prerequisites = {
    # Most Basic - Foundation Level
    "Basics": ["Foundation"],  # No prerequisites - this IS the foundation
    
    # Level 2 - Build on Basics
    "Sorting Techniques": ["Basics"],
    "Arrays": ["Basics"],
    "Strings [Basic and Medium, Strings]": ["Basics", "Arrays"],
    "Linked List": ["Basics"],
    "Recursion": ["Basics"],
    "Bit Manipulation": ["Basics"],
    
    # Level 3 - Intermediate Topics
    "Binary Search": ["Arrays", "Sorting Techniques"],
    "Stack and Queues": ["Arrays", "Linked List"],
    "Sliding Window & Two Pointer": ["Arrays", "Strings [Basic and Medium, Strings]"],
    
    # Level 4 - Advanced Data Structures
    "Binary Trees": ["Recursion", "Linked List"],
    "Heaps": ["Arrays", "Binary Trees"],
    
    # Level 5 - Complex Topics
    "Binary Search Trees": ["Binary Trees", "Binary Search"],
    "Greedy Algorithms": ["Sorting Techniques", "Arrays"],
    "Graphs": ["Arrays", "Recursion", "Stack and Queues", "Binary Trees"],
    "Tries": ["Binary Trees", "Strings [Basic and Medium, Strings]"],
    
    # Level 6 - Most Advanced
    "Dynamic Programming": ["Recursion", "Arrays", "Strings [Basic and Medium, Strings]"],
    "String": ["Strings [Basic and Medium, Strings]", "Dynamic Programming"]  # Hard string problems
}