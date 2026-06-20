import random

basic_responses = {
    "hello": [
        "Hello! How can I assist you today?",
        "Hi there! Ready to learn something new?",
        "Hey! Hope you're having a productive day."
    ],

    "hi": [
        "Hi!",
        "Hello!",
        "Greetings!"
    ],

    "how are you": [
        "I'm doing great! Thanks for asking.",
        "I'm always ready to help students.",
        "Doing well! How about you?"
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help.",
        "Glad I could assist."
    ],

    "study tips": [
        "Study consistently for short intervals.",
        "Use active recall and spaced repetition.",
        "Practice problems regularly."
    ],

    "cgpa tips": [
        "Attend classes regularly.",
        "Revise weekly.",
        "Focus on understanding concepts."
    ],

    "placement tips": [
        "Practice aptitude and DSA daily.",
        "Build projects and maintain GitHub.",
        "Prepare HR questions."
    ],

    "resume tips": [
        "Keep it concise.",
        "Highlight projects and internships.",
        "Include measurable achievements."
    ],

    "interview tips": [
        "Be confident.",
        "Explain your projects clearly.",
        "Practice mock interviews."
    ],

    "python tips": [
        "Master functions and OOP.",
        "Practice problem solving.",
        "Work on projects."
    ],

    "github tips": [
        "Write proper README files.",
        "Commit regularly.",
        "Keep repositories organized."
    ],

    "hackathon tips": [
        "Build MVP first.",
        "Divide work efficiently.",
        "Manage time wisely."
    ],

    "aptitude tips": [
        "Practice ratios and percentages.",
        "Solve puzzles regularly.",
        "Track your speed."
    ],

    "hr questions": [
        "Prepare Tell me about yourself.",
        "Know your strengths and weaknesses.",
        "Research the company."
    ]
}

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself.",
    "Dream big and work hard.",
    "Consistency beats intensity."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why couldn't the computer take its hat off? Because it had CAPS LOCK on.",
    "Why do Java developers wear glasses? Because they don't C#."
]


def get_random_response(category):
    return random.choice(basic_responses[category])


def get_quote():
    return random.choice(quotes)


def get_joke():
    return random.choice(jokes)