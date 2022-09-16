"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name: Tim Osmond
Date started: 23/04/22

Pseudocode:
function main()
    print "Welcome message"
    print "Would you like to load your plants from file"
    (check for default "Y")
    if yes
        load plants file()
        print "loaded, plants"
        plants = file
        number of plants = 0
        length of plants = 0
        for plant in plants
            Count characters of plants
            Count number of plants
        print "plants"
        total food = 0
        day = 0
        print "day, number of plants, total food"
    else:
        plants = "Parsley, Sage, Rosemary, Thyme"
        number of plants = 0
        length of plants = 0
        count number of plants
        print "You start with these plants:"
        print "plants"
        total food = 0
        day = 0
        print daily totals()
    print "menu"
    get choice
    while choice != "Q"
        if choice is "W"
            if number of plants = 0
                print "All your plants are dead! You need to buy more or
                go to Coles!"
                print daily totals()
            else
                function simulate day()
                print "rainfall"
                if day rainfall < death level
                    fetch random plant from plants
                    kill random plant()
                    count number of plants
                    print "Sadly, your random plant has died."
                    if number of plants = 0
                        print "All your plants are dead! You need to buy more or
                        go to Coles!"
                        print daily totals()
                    else
                        food per plant = 0
                        total food = 0
                        print daily totals()
                else
                    calculate percentage()
                    calculate food per plant()
                    print daily totals()
        elif choice = "D"
            print plants list
            print daily totals()
        elif choice = "A"
            (Title case)
            (Check for getting caught in loop if food is zero)
            print = "Enter plant name"
                check plant expense()
                check plant exists()
                add new plant()
        else
            print "Invalid choice."
            print daily totals()
        menu()

    print "Would you like to save your plants to plants.txt (Y/n): "
    (Check for default "Y")
    if yes
        save to plant file()
        thank you()
    else
        thank you()

function simulate day()
    day + 1
    min rainfall = 0
    max rainfall = 128
    rainfall()
    return "rainfall, day"

function print menu()
    MENU = "(W)ait (D)isplay (A)dd (Q)uit"
    print "MENU"
    get choice
    return choice


function kill random plant(number of plants, plants)
    percentage = 0
    delete plant = random number between 0 and number of plants - 1
    dead plant = plants[delete plant]
    return dead plant, delete plant, percentage


function load plants file()
    in_file = open plants.txt
    plants = []
    for each line in in_file
        plant = individual line
        append to plants list
    in_file.close()
    return plants


function add new plant(days, new plant, number of plants, plants, total food)
    if new plant != ""
        add new plant to plant
        cost = characters in new plant
        total food = total food - cost
        number of plants = count number of plants
        print daily totals
    return number of plants, total food


function check plant exists(new plant, plants)
    if new plant != ""
        while new plant in plants
            print("Plant already exists, choose another.")
            new plant = input("Enter plant name or Enter to skip: ").title()
    return new plant


function check plant expense(new plant, total food)
    if new plant != ""
        while length of new plant > total food
            print "new plant would cost 'length of new plant' food. With only 'total food', you can't afford it."
            print "Enter plant name or Enter to skip: "
    return new plant


function save to plant file(plants)
    out_file = open plants.txt
    for plant in plants
        (Print each plant on a new line)
    out_file.close()

function thank you()
    print("Thank you for simulating, now enjoy some real plants.")


function print daily totals(days, number of plants, total food)
    print "After 'days' day(s), you have 'number of plants' plant(s) and your total food is 'total food'.")


function calculate food per plant(percentage, plants, total food)
    for plant in plants
        food per plant = percentage * characters in plant
        print "'plant' produced 'food per plant end"
        total food = total food + food_per_plant
    return total food


function calculate percentage(day rainfall)
    percentage = random between (day rainfall/3 and day rainfall)/128
    return percentage


function rainfall()
    day rainfall = random number between minimum rainfall and maximum rainfall
    return day rainfall

The Market Garden Simulator is a program that simulates the tranquil and refreshing
activity of growing your own garden for fun and profit. You have a list of plants,
which each generate "food" according to their name length (as everyone knows,
longer plant names mean higher profit at market… but they cost more to buy). Each day
when you wait and watch, it rains a random amount.
This rainfall determines how much food the plants generate, but if you don't get enough rain,
a random plant will die. When you have enough food, you can buy new plants. To increase the
biodiversity of your garden, you can't buy plants you already have.
The program starts with a welcome, some instructions and initial plants. You can choose to either
load existing plants from a text file or start with four standard plants.
Notice the form of the prompt for this and saving plants at is “Y/n” which means that Yes
is the default. Anything other than N or n is interpreted as a Yes.
"""

import random

MENU = "\n(W)ait\n(D)isplay\n(A)dd\n(Q)uit"
MIN_RAIN = 0  # The minimum amount it will rain in a day
MAX_RAIN = 128  # The maximum amount it will rain in a day
DEATH_RAIN_LEVEL = 32  # Below this level of rain will kill a plant


def main():
    """Market Garden Simulator program."""
    plants = ["Parsley", "Sage", "Rosemary", "Thyme"]  # Default list of plants
    days = 0  # Used for day count
    total_food = 0  # Used for food addition
    length_of_plants = 0  # Used to calculate length of plant names
    number_of_plants = 0  # Used to calculate number of plants

    print("Welcome to your garden.\nPlants cost and generate food according to their name"
          "length (e.g., Sage plants cost 4).\nYou can buy new plants with the food"
          " your garden generates.\nYou get up to 128 mm of rain per day. Not all "
          "plants can survive with less than 32mm.\nEnjoy:)")

    load_plants = input("Would you like to load your plants from plants.txt (Y/n): ").lower()
    if not load_plants == "n":
        print("Loaded.\nYou start with these plants:")
        plants = load_plants_file()
        for plant in plants:
            # Count characters of plants
            length_of_plants = count_number_plants(length_of_plants, plant)
            # Count number of plants
        number_of_plants = count_number_plants(number_of_plants, plants)
        print_plants_list(plants)
        print_daily_totals(days, number_of_plants, total_food)
    else:
        number_of_plants = count_number_plants(number_of_plants, plants)  # Count number of plants
        print("You start with these plants:")
        print_plants_list(plants)
        print_daily_totals(days, number_of_plants, total_food)
    choice = print_menu()
    while choice != "Q":
        if choice == "W":  # Wait a day and add rainfall
            if number_of_plants == 0:  # Print if there are no plants left
                print("All your plants are dead! You need to buy more or go to Coles!")
                print_daily_totals(days, number_of_plants, total_food)
            else:
                days += 1  # Add a day to the number of days
                day_rainfall = rainfall()  # Fetch the random rainfall for this day
                print(f"\nRainfall: {day_rainfall}mm")
                if day_rainfall < DEATH_RAIN_LEVEL:  # Check if rainfall is below the CONSTANT
                    # Fetch random plant from plants
                    dead_plant, delete_plant, percentage = \
                        kill_random_plant(number_of_plants, plants)
                    del plants[delete_plant]  # Delete random plant from list
                    number_of_plants = len(plants)
                    print(f"Sadly, your {dead_plant} plant has died.")
                    if number_of_plants == 0:  # Print if there are no plants left
                        print("All your plants are dead! You need to buy more or go to Coles!")
                        print_daily_totals(days, number_of_plants, total_food)
                    else:  # Calculate zero food for the day and print plants
                        total_food = calculate_food_per_plant(percentage, plants, total_food)
                else:
                    # Get percentage for food calculation
                    percentage = calculate_percentage(day_rainfall)
                    # Calculate the food per plant using percentage
                    total_food = calculate_food_per_plant(percentage, plants, total_food)
                    print_daily_totals(days, number_of_plants, total_food)
        elif choice == "D":
            print_plants_list(plants)
            print_daily_totals(days, number_of_plants, total_food)
        elif choice == "A":
            #  Exit for empty string otherwise caught in loop if no food available
            new_plant = input("Enter plant name or Enter to skip: ").title()
            # Check plant price is not greater than food available
            new_plant = check_plant_expense(new_plant, total_food)
            # Check plant does not already exist
            new_plant = check_plant_exists(new_plant, plants)
            # Add plant to list of plants
            number_of_plants, total_food = \
                add_new_plant(days, new_plant, number_of_plants, plants, total_food)
        else:
            print("Invalid choice.")
            print_daily_totals(days, number_of_plants, total_food)
        choice = print_menu()
    print_daily_totals(days, number_of_plants, total_food)
    save_file = input("Would you like to save your plants to plants.txt (Y/n): ").lower()
    # If anything but "n", save the file
    if not save_file == "n":
        save_to_plant_file(plants)
        print("Saved.")
        thank_you()
    else:
        thank_you()


def print_menu():
    """Prints the menu with choice"""
    print(MENU)
    choice = input("Choose: ").upper()
    return choice


def kill_random_plant(number_of_plants, plants):
    """Set food percentage to zero and delete the plant from the list."""
    percentage = 0  # Set stored percentage to zero for all plants calculations
    delete_plant = random.randint(0, number_of_plants - 1)  # Choose a random plant from list
    dead_plant = plants[delete_plant]  # Find the random plant in the list
    return dead_plant, delete_plant, percentage


def load_plants_file():
    """Open the plants file and read the list of plants."""
    in_file = open("plants.txt")
    plants = []  # Clear plants list stored variable
    for line in in_file:
        plant = line.strip()  # Read each line of file
        plants.append(plant)  # Create a list from file lines
    in_file.close()
    return plants


def add_new_plant(days, new_plant, number_of_plants, plants, total_food):
    """Add a new plant to the list and display details of list."""
    if new_plant != "":
        plants.append(new_plant)
        cost = len(new_plant)  # Number of characters in name is cost
        total_food -= cost  # Subtract cost from the food total
        number_of_plants = len(plants)
        print_daily_totals(days, number_of_plants, total_food)
    return number_of_plants, total_food


def check_plant_exists(new_plant, plants):
    """Check if the plant already exists in the list."""
    if new_plant != "":
        while new_plant in plants:
            print("Plant already exists, choose another.")
            new_plant = input("Enter plant name or Enter to skip: ").title()
    return new_plant


def check_plant_expense(new_plant, total_food):
    """Check there is enough food to buy a plant of entered length, printing message."""
    if new_plant != "":
        while len(new_plant) > total_food:  # Check number of characters are not greater than food
            print(f"{new_plant} would cost {len(new_plant)} food. With only "
                  f"{total_food}, you can't afford it.")
            new_plant = input("Enter plant name or Enter to skip: ").title()
    return new_plant


def save_to_plant_file(plants):
    """Save to the plants file on exit."""
    out_file = open("plants.txt", "w")
    for plant in plants:
        # Print each plant on a new line
        print(plant, end='\n', file=out_file)
    out_file.close()


def count_number_plants(number_of_plants, plants):
    """Count the number of plants in the list."""
    number_of_plants += len(plants)
    return number_of_plants


def print_plants_list(plants):
    """Print the list of plants separated by commas."""
    print(*plants, sep=", ")  # Print comma separated from list


def thank_you():
    """Print the exit message"""
    print("Thank you for simulating, now enjoy some real plants.")


def print_daily_totals(days, number_of_plants, total_food):
    """Print the daily summary."""
    print(f"\nAfter {days} day(s), you have {number_of_plants} "
          f"plant(s) and your total food is {total_food}.")


def calculate_food_per_plant(percentage, plants, total_food):
    """Calculate the food from the length of each plant and percentage increase."""
    for plant in plants:
        #  Round the food totals as integers
        food_per_plant = int(round(percentage * len(plant), 0))
        print(plant, "produced", food_per_plant, end=', ')
        total_food += food_per_plant  # Add totals from each plant to food
    return total_food


def calculate_percentage(day_rainfall):
    """Calculate the percentage increase to be used on each plant."""
    percentage = random.randint(int(day_rainfall / 3), day_rainfall + 1) / 128
    return percentage


def rainfall():
    """Calculate the random rainfall for the day."""
    day_rainfall = random.randint(MIN_RAIN, MAX_RAIN + 1)
    return int(day_rainfall)


# def tests():
# plants = ["1234567890", "12345"]
# calculate_food_per_plant(10, plants, 0)

# day_rainfall = 0  # Choose this one or line below to test
# # day_rainfall = rainfall()
# total_food = 0
# plants = ["Parsley", "Sage", "Rosemary", "Thyme", "Broccolini"]
# percentage = calculate_percentage(day_rainfall)
# calculate_food_per_plant(percentage, plants, total_food)
# print(f"\nRainfall: {day_rainfall}")
# print(f"Random = {percentage * 128}")
# print(f"Third of rainfall: {int(day_rainfall / 3)}")
# print(f"Percentage: {percentage}")
# print(
#     f"Parsley: {percentage * len('Parsley')}, Sage: {percentage * len('Sage')}, "
#     f"Rosemary: {percentage * len('Rosemary')}, Thyme: {percentage * len('Thyme')}, "
#     f"Broccolini: {percentage * len('Broccolini')}, ")

# plants = []
# number_of_plants = 0
# number_of_plants = count_number_plants(number_of_plants, plants)
# print(f" None: {number_of_plants}")
# plants = [" "]
# number_of_plants = 0
# number_of_plants = count_number_plants(number_of_plants, plants)
# print(f" Space = 1: {number_of_plants}")
# plants = [" ", "A"]
# number_of_plants = 0
# number_of_plants = count_number_plants(number_of_plants, plants)
# print(f" 2: {number_of_plants}")


# tests()
main()
