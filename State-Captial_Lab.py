import random

def play_game():
    # Shuffle the states randomly
    random.shuffle(states)
    
    # Initialize tallies for correct and incorrect answers
    correct_answers = 0
    incorrect_answers = 0
    
    # Iterate through all the states
    for state in states:
        state_name = state["name"]
        capital = state["capital"]
        
        # Prompt the user for the capital of the state
        user_answer = input(f"What is the capital of {state_name}? ")
        
        # Check if the user's answer is correct
        if user_answer.lower() == capital.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The capital of {state_name} is {capital}.")
            incorrect_answers += 1
        
        # Display the tally for the current state
        total_answers = correct_answers + incorrect_answers
        print(f"You have answered {correct_answers} out of {total_answers} correctly for {state_name}.")
        print()
    
    # After going through all the states, ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        play_game()

# Welcome message
print("Welcome to the State Capitals Game!")
print("You will be prompted to guess the capital of each state.")

# The updated array of states
states = [
    {
        "name": "Alabama",
        "capital": "Montgomery"
    }, {
        "name": "Alaska",
        "capital": "Juneau"
    }, {
        "name": "Arizona",
        "capital": "Phoenix"
    }, {
        "name": "Kentucky",
        "capital": "Frankfort"
    }, {
        "name": "Louisiana",
        "capital": "Baton Rouge"
    }, {
        "name": "Maine",
        "capital": "Augusta"
    }, {
        "name": "Maryland",
        "capital": "Annapolis"
    }, {
        "name": "Massachusetts",
        "capital": "Boston"
    }, {
        "name": "Michigan",
        "capital": "Lansing"
    }, {
        "name": "Minnesota",
        "capital": "St. Paul"
    }, {
        "name": "Mississippi",
        "capital": "Jackson"
    }, {
        "name": "Missouri",
        "capital": "Jefferson City"
    }, {
        "name": "Montana",
        "capital": "Helena"
    }, {
        "name": "Nebraska",
        "capital": "Lincoln"
    }, {
        "name": "Nevada",
        "capital": "Carson City"
    }, {
        "name": "New Hampshire",
        "capital": "Concord"
    }, {
        "name": "New Jersey",
        "capital": "Trenton"
    }, {
        "name": "New Mexico",
        "capital": "Santa Fe"
    }
]

# Start the game
play_game()
