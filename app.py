"""
PiDog Final Project
Interactive AI-Powered Robotic Performer

Main Application
"""

from ai.ollama_brain import ask_pidog
from shows.introduction_show import run_introduction_show
from ai.pidog_reactions import (
    thinking_reaction,
    happy_reaction,
    listening_reaction
)

from ai.command_handler import handle_command

from shows.show_manager import run_performance
from pidog_controller import PiDogController


# =================================================
# MAIN MENU
# =================================================

def show_menu():

    print("\n" + "=" * 55)
    print("PIDOG FINAL PROJECT")
    print("Interactive AI-Powered Robotic Performer")
    print("=" * 55)

    print("\n1. PiDog Introduction")
    print("2. Performance Mode")
    print("3. AI Q&A Mode")
    print("4. Exit")


# =================================================
# PIDOG INTRODUCTION
# =================================================

def introduction(dog):

    run_introduction_show(dog)


# =================================================
# PERFORMANCE MODE
# =================================================

def performance_mode(dog):

    run_performance(dog)


# =================================================
# AI Q&A MODE
# =================================================

def ai_mode(dog):

    print("\n" + "=" * 55)
    print("PIDOG AI Q&A MODE")
    print("=" * 55)

    print("\nYou can ask PiDog questions or give commands.")
    print("Examples: dance, perform, sit, stand, wag your tail")
    print("Type 'exit' to return to the Main Menu.")

    while True:

        # PiDog waits for the user
        listening_reaction(dog)

        question = input("\nYou: ").strip()

        # ---------------------------------------------
        # EXIT AI MODE
        # ---------------------------------------------

        if question.lower() == "exit":

            print("\nReturning to Main Menu...")

            break

        # Ignore empty input
        if not question:

            continue

        # ---------------------------------------------
        # CHECK FOR ROBOT COMMAND
        # ---------------------------------------------

        command_executed = handle_command(
            question,
            dog
        )

        # If PiDog performed a command,
        # return to listening mode.
        if command_executed:

            print("\nPiDog completed the command.")

            continue

        # ---------------------------------------------
        # AI THINKING REACTION
        # ---------------------------------------------

        thinking_reaction(dog)

        # Ask Ollama
        answer = ask_pidog(question)

        # Show AI response
        print(f"\nPiDog: {answer}")
        dog.speak(answer)

        # Happy reaction
        happy_reaction(dog)


# =================================================
# MAIN PROGRAM
# =================================================

def main():

    print("\nStarting PiDog Final Project...")

    dog = PiDogController()

    try:

        while True:

            show_menu()

            choice = input(
                "\nSelect an option (1-4): "
            ).strip()

            # =========================================
            # PIDOG INTRODUCTION
            # =========================================

            if choice == "1":

                introduction(dog)


            # =========================================
            # PERFORMANCE MODE
            # =========================================

            elif choice == "2":

                performance_mode(dog)


            # =========================================
            # AI Q&A MODE
            # =========================================

            elif choice == "3":

                ai_mode(dog)


            # =========================================
            # EXIT
            # =========================================

            elif choice == "4":

                print("\nGoodbye!")

                break


            # =========================================
            # INVALID INPUT
            # =========================================

            else:

                print(
                    "\nInvalid choice. Please select 1-4."
                )

    except KeyboardInterrupt:

        print("\n\nProgram stopped by user.")

    finally:

        dog.close()


# =================================================
# START APPLICATION
# =================================================

if __name__ == "__main__":

    main()