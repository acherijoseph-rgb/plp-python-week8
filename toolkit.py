# Personal Mini-Toolkit
# This program provides several simple tools through a menu.

print("========================================")
print("       WELCOME TO MY MINI-TOOLKIT")
print("========================================")
print("Choose a tool and have fun!")


while True:
    print("\nPlease choose a tool:")
    print("1. Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Name Formatter")
    print("5. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        # Calculator: performs basic arithmetic on two numbers.
        print("\n--- Calculator ---")

        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Sorry, you cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print(f"Sorry, '{operator}' is not a valid operation.")
                continue

            print(f"Your answer is: {result}")

        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "2":
        # To-Do List: lets the user add, view, and remove tasks.
        print("\n--- To-Do List ---")

        tasks = []

        while True:
            print("\n1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Return to main menu")

            todo_choice = input("Choose an option: ")

            if todo_choice == "1":
                task = input("Enter a task: ")
                tasks.append(task)
                print(f"Task added: {task}")

            elif todo_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif todo_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    try:
                        task_number = int(
                            input("Enter the task number to remove: ")
                        )

                        if 1 <= task_number <= len(tasks):
                            removed_task = tasks.pop(task_number - 1)
                            print(f"Removed task: {removed_task}")
                        else:
                            print("That task number is not on the list.")

                    except ValueError:
                        print("Please enter a valid task number.")

            elif todo_choice == "4":
                print("Returning to the main menu.")
                break

            else:
                print(f"Sorry, '{todo_choice}' is not a valid option.")

    elif choice == "3":
        # Number Guessing Game: keeps asking until the player guesses correctly.
        print("\n--- Number Guessing Game ---")

        secret_number = 7
        attempts = 0

        print("I am thinking of a number between 1 and 10.")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(
                        f"Correct! You guessed the number in "
                        f"{attempts} attempts."
                    )
                    break

            except ValueError:
                print("Please enter a whole number.")

    elif choice == "4":
        # Name Formatter: formats a person's name in a clean way.
        print("\n--- Name Formatter ---")

        name = input("Enter your full name: ")
        formatted_name = name.strip().title()

        if formatted_name:
            print(f"Your formatted name is: {formatted_name}")
        else:
            print("You did not enter a name.")

    elif choice == "5":
        print("\nThanks for using my Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")