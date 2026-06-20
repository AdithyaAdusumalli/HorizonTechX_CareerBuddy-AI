import datetime
import os

CHAT_FILE = "chat_history.txt"


def save_chat(user, bot):
    with open(CHAT_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"\n[{timestamp}]\n")
        file.write(f"You: {user}\n")
        file.write(f"CareerBuddy AI: {bot}\n")


def show_history():
    if not os.path.exists(CHAT_FILE):
        print("\nNo chat history found.")
        return

    with open(CHAT_FILE, "r", encoding="utf-8") as file:
        history = file.read()

    print("\n===== CHAT HISTORY =====")

    if history.strip():
        print(history)
    else:
        print("No conversations yet.")


def clear_history():
    with open(CHAT_FILE, "w", encoding="utf-8"):
        pass

    print("\nChat history cleared successfully.")


def get_time():
    return datetime.datetime.now().strftime(
        "Current Time: %I:%M:%S %p"
    )


def get_date():
    return datetime.datetime.now().strftime(
        "Today's Date: %d-%m-%Y"
    )