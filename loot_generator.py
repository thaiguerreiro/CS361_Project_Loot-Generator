import random


# Constants for loot categories and rarities
CATEGORIES = ["Weapon", "Armor", "Accessory"]
RARITIES = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
LOW_RARITY_MODIFIERS = ['Rusty', 'Worn', 'Old', 'Dull', 'Cracked', 'Wooden']
MID_RARITY_MODIFIERS = ['Silver', 'Golden', 'Bronze', 'Crystal', 'Obsidian', 'Iron', 'Steel']
HIGH_RARITY_MODIFIERS = [
                          {"name": "Embersteel",
                          "description": "forged in the heart of a volcano, causing it to radiate heat and power.",
                          "statType": "Damage",
                          "stat": 10,
                          "trait": "Fire Affinity"},

                         {"name": "Shadowfang",
                          "description": "imbued with the essence of darkness, allowing it to strike fear into the hearts of enemies.",
                          "statType": "Damage",
                          "stat": 15,
                          "trait": "Stealth Enhancement"},

                         {"name": "Stormbreaker",
                          "description": "imbued with the power of stores, causing it to vibrate with electricity.",
                          "statType": "Damage",
                          "stat": 10,
                          "trait": "Lightning Affinity"},

                         {"name": "Frostwood",
                          "description": "carved from the heart of an ancient glacier, providing insulation and strength.",
                          "statType": "Defense",
                          "stat": 20,
                          "trait": "Ice Affinity"},

                         {"name": "Stoneheart",
                          "description": "crafted from the hardest stone, making it incredibly durable and resistant to damage.",
                          "statType": "Defense",
                          "stat": 25,
                          "trait": None},

                         {"name": "Blazing",
                          "description": "enchanted with the essence of fire, causing it to emit intense heat and flames. Grants the bearer A",
                          "statType": None,
                          "stat": None,
                          "trait": "Burns nearby foes"}
                         ]


# Function to display the main menu header
def MainMenuHeader():
    print("\n--------------------------------------------\n")
    print("               Loot Generator               ")
    print("\n--------------------------------------------\n")
    
    print("Welcome to the random loot generator!\n")
    print("Generate fantasy items for your game or use")
    print("random generation to discover unexpected loot.\n")
    
    print("To generate an item:")
    print("   1. Choose a loot category")
    print("   2. Review the generated item")
    print("   3. Save, discard, or return to the menu")


# Function to display the main menu options
def MainMenu():
    print("\n--------------------------------------------\n")
    
    print("   1. Choose a Category")
    print("   2. Generate Random Loot")
    print("   3. Exit\n")
    
    print("Select an option (1-3): ", end="")


# Function to display the category selection menu
def ChooseCategory():
    print("\n--------------------------------------------\n")

    print("Choose a loot category to generate, or Random")
    print("to let the generator choose for you.\n")

    print("   1. Weapon")
    print("   2. Armor")
    print("   3. Accessory")
    print("   4. Random")
    print("   5. Return to Main Menu\n")

    print("Select an option (1-5): ", end="")


# Function to display the generated loot header
def GeneratedLootHeader():
    print("\n--------------------------------------------\n")
    print("               Generated Loot")
    print("\n--------------------------------------------\n")


# Function to display the generated loot details
def LootSummary(name, type, rarity, stat, statType, durability, trait):
    print(f"Name: {name}")
    print(f"Type: {type}")
    print(f"Rarity: {rarity}\n")

    print(f"{statType}: {stat}")
    print(f"Durability: {durability}")
    if trait:
        print(f"Trait: {trait}")


# Function to generate random loot based on the selected category
def GenerateLoot(category):
    if category == "Weapon":
        type = "Weapon"
        rarity = random.choice(RARITIES)

        # Determine stat modifier based on rarity
        if rarity == "Common":
            modifier = random.choice(LOW_RARITY_MODIFIERS)
            statModifier = 0.25
        elif rarity == "Uncommon":
            modifier = random.choice(MID_RARITY_MODIFIERS)
            statModifier = 0.5
        elif rarity == "Rare":
            modifier = random.choice(MID_RARITY_MODIFIERS)
            statModifier = 0.75
        elif rarity == "Epic":
            modifier = random.choice(HIGH_RARITY_MODIFIERS)
            statModifier = 1.0
        else:  # Legendary
            modifier = random.choice(HIGH_RARITY_MODIFIERS)
            statModifier = 1.5

        name = f"{modifier} {random.choice(['Sword', 'Axe', 'Bow', 'Dagger'])}"
        stat = random.randint(50, 100) * statModifier
        statType = "Damage"
        durability = random.randint(50, 100) * statModifier

        


# Main function to run the loot generator program
def main():
    mainMenuChoice = 0
    categoryChoice = 0

    MainMenuHeader() # Display the main menu header

    # Loop to keep the program running until the user chooses to exit
    while mainMenuChoice != 3:
        MainMenu() # Display the main menu options

        # Get user input for the main menu choice and handle invalid input
        try:
            mainMenuChoice = int(input())
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 3.")
            continue

        match mainMenuChoice:
            case 1: # Choose a category
                # Choose a category logic here
                pass
            case 2: # Generate random loot
                # Generate random loot logic here
                pass
            case 3: # Exit the program
                pass
            case _: # Handle invalid menu choice
                print("\nInvalid choice. Please select a valid option.")

    print("\nThank you for using this loot generator. Goodbye!")
        

# Entry point of the program
if __name__ == "__main__":
    main()