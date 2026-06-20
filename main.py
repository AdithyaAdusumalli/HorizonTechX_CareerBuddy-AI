from responses import (
    get_random_response,
    get_quote,
    get_joke,
    basic_responses
)

from utils import (
    save_chat,
    show_history,
    clear_history,
    get_time,
    get_date
)


print("\n🎓 Welcome to CareerBuddy AI Pro")
print("Type 'commands' to view all commands.\n")


while True:

    user_input = input("You: ").strip().lower()

    response = ""

    # Basic Responses
    if user_input in basic_responses:
        response = get_random_response(user_input)

    # Smart Utilities
    elif "motivate" in user_input or "quote" in user_input:
        response = get_quote()

    elif "joke" in user_input:
        response = get_joke()

    elif "time" in user_input:
        response = get_time()

    elif "date" in user_input:
        response = get_date()

    # History
    elif user_input == "history":
        show_history()
        continue

    elif user_input == "clear history":
        clear_history()
        continue

    # Information
    elif user_input == "about":
        response = (
            "CareerBuddy AI Pro is a Python-based assistant "
            "for students preparing for academics, placements, "
            "and hackathons."
        )

    elif user_input == "creator":
        response = (
            "Developed as an internship-ready educational chatbot."
        )

    elif user_input == "version":
        response = "CareerBuddy AI Pro v1.0"

    elif user_input in ["commands", "help"]:
        response = (
            "\nAvailable Commands:\n"
            "hello\n"
            "hi\n"
            "how are you\n"
            "thanks\n"
            "study tips\n"
            "cgpa tips\n"
            "placement tips\n"
            "resume tips\n"
            "interview tips\n"
            "python tips\n"
            "github tips\n"
            "hackathon tips\n"
            "aptitude tips\n"
            "hr questions\n"
            "motivate me\n"
            "quote\n"
            "joke\n"
            "time\n"
            "date\n"
            "history\n"
            "clear history\n"
            "about\n"
            "creator\n"
            "version\n"
            "bye\n"
            "exit"
        )

    # Exit
    elif user_input in ["bye", "exit"]:
        response = (
            "Goodbye! Wishing you success in your studies, "
            "placements, and future career."
        )

        print("\nCareerBuddy AI:", response)

        save_chat(user_input, response)

        break

    # Mini AI Keyword Matching
    elif "placement" in user_input:
        response = get_random_response("placement tips")

    elif "resume" in user_input:
        response = get_random_response("resume tips")

    elif "interview" in user_input:
        response = get_random_response("interview tips")

    elif "python" in user_input:
        response = get_random_response("python tips")

    elif "hackathon" in user_input:
        response = get_random_response("hackathon tips" or "Hackathon tips" or "HACKATHON TIPS" or "Hackathon Tips")

    elif "study" in user_input:
        response = get_random_response("study tips")

    else:
        response = (
            "Sorry, I didn't understand that.\n"
            "Type 'commands' to see available options."
        )

    print("\nCareerBuddy AI:", response)

    save_chat(user_input, response)