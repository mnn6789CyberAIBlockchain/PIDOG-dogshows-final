"""
PiDog Final Project
Show Manager

Controls individual performances and the
complete PiDog Final Performance.
"""

import time

from shows.introduction_show import run_introduction_show
from shows.christmas_show import run_christmas_show
from shows.pokemon_show import run_pokemon_show
from shows.interactive_show import run_interactive_show
from shows.final_qa import run_final_qa
from shows.demo_show import run_demo_show


# =================================================
# PERFORMANCE MENU
# =================================================

def performance_menu():

    print("\n" + "=" * 55)
    print("PIDOG PERFORMANCE MODE")
    print("=" * 55)

    print("\n1. Complete Final Performance")
    print("2. PiDog Introduction")
    print("3. Christmas Show")
    print("4. Pokemon Show")
    print("5. Interactive Human-PiDog Show")
    print("6. Final AI Q&A")
    print("7. Demo Performance")
    print("8. Return to Main Menu")


# =================================================
# REST BETWEEN PERFORMANCES
# =================================================

def rest_between_shows(dog):

    print("\n" + "-" * 55)
    print("PiDog is resting before the next performance...")
    print("-" * 55)

    # Low/resting posture
    dog.action(
        "lie",
        speed=80
    )

    # Give the servos time to settle
    time.sleep(2)


# =================================================
# PREPARE FOR NEXT PERFORMANCE
# =================================================

def prepare_for_show(dog):

    print("\nPiDog is preparing for the next performance...")

    dog.stand(
        speed=110
    )

    time.sleep(1)


# =================================================
# COMPLETE FINAL PERFORMANCE
# =================================================

def run_complete_performance(dog):

    print("\n" + "=" * 60)
    print("STARTING COMPLETE PIDOG FINAL PERFORMANCE")
    print("=" * 60)

    # =============================================
    # PART 1 — INTRODUCTION
    # =============================================

    print("\n[PART 1] PIDOG INTRODUCTION")

    run_introduction_show(dog)

    # REST
    rest_between_shows(dog)

    # =============================================
    # PART 2 — CHRISTMAS
    # =============================================

    print("\n[PART 2] CHRISTMAS PERFORMANCE")

    prepare_for_show(dog)

    run_christmas_show(dog)

    # REST
    rest_between_shows(dog)

    # =============================================
    # PART 3 — POKEMON
    # =============================================

    print("\n[PART 3] POKEMON PERFORMANCE")

    prepare_for_show(dog)

    run_pokemon_show(dog)

    # REST
    rest_between_shows(dog)

    # =============================================
    # PART 4 — INTERACTIVE
    # =============================================

    print("\n[PART 4] INTERACTIVE HUMAN-PIDOG PERFORMANCE")

    prepare_for_show(dog)

    run_interactive_show(dog)

    # REST
    rest_between_shows(dog)

    # =============================================
    # PART 5 — FINAL AI Q&A
    # =============================================

    print("\n[PART 5] LIVE AI Q&A")

    prepare_for_show(dog)

    run_final_qa(dog)

    # =============================================
    # COMPLETE
    # =============================================

    print("\n" + "=" * 60)
    print("COMPLETE PERFORMANCE FINISHED!")
    print("=" * 60)

    dog.set_light(
        "green",
        bps=2
    )

    dog.sit(
        speed=110
    )


# =================================================
# PERFORMANCE MODE
# =================================================

def run_performance(dog):

    while True:

        performance_menu()

        choice = input(
            "\nSelect a performance (1-8): "
        ).strip()


        # =============================================
        # OPTION 1 — COMPLETE FINAL PERFORMANCE
        # =============================================

        if choice == "1":

            run_complete_performance(dog)

            input(
                "\nPress ENTER to return to "
                "the Performance Menu..."
            )


        # =============================================
        # OPTION 2 — INTRODUCTION
        # =============================================

        elif choice == "2":

            print(
                "\nStarting PiDog Introduction..."
            )

            run_introduction_show(dog)

            input(
                "\nPress ENTER to continue..."
            )


        # =============================================
        # OPTION 3 — CHRISTMAS
        # =============================================

        elif choice == "3":

            print(
                "\nStarting Christmas Show..."
            )

            run_christmas_show(dog)

            input(
                "\nPress ENTER to continue..."
            )


        # =============================================
        # OPTION 4 — POKEMON
        # =============================================

        elif choice == "4":

            print(
                "\nStarting Pokemon Show..."
            )

            run_pokemon_show(dog)

            input(
                "\nPress ENTER to continue..."
            )


        # =============================================
        # OPTION 5 — INTERACTIVE
        # =============================================

        elif choice == "5":

            print(
                "\nStarting Interactive "
                "Human-PiDog Show..."
            )

            run_interactive_show(dog)

            input(
                "\nPress ENTER to continue..."
            )


        # =============================================
        # OPTION 6 — FINAL AI Q&A
        # =============================================

        elif choice == "6":

            print(
                "\nStarting Final AI Q&A..."
            )

            run_final_qa(dog)

            input(
                "\nPress ENTER to continue..."
            )


        # =============================================
        # OPTION 7 — DEMO
        # =============================================

        elif choice == "7":

            print(
                "\nStarting Demo Performance..."
            )

            run_demo_show(dog)

            input(
                "\nPress ENTER to continue..."
            )


        # =============================================
        # OPTION 8 — RETURN
        # =============================================

        elif choice == "8":

            print(
                "\nReturning to Main Menu..."
            )

            break


        # =============================================
        # INVALID INPUT
        # =============================================

        else:

            print(
                "\nInvalid choice. Please select 1-8."
            )