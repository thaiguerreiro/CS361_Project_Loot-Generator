import random
import json
import os
import textwrap


# Constants for loot categories and rarities
CATEGORIES = ["Weapon", "Armor", "Accessory"]
RARITIES = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
LOW_RARITY_MODIFIERS = ['Rusty', 'Worn', 'Old', 'Dull', 'Cracked', 'Wooden']
MID_RARITY_MODIFIERS = ['Silver', 'Golden', 'Bronze', 'Crystal', 'Obsidian', 'Iron', 'Steel']
HIGH_RARITY_MODIFIERS = [
                          {"name": "Embersteel",
                          "description": "forged in the heart of a volcano, causing it to radiate heat and power.",
                          "bonus": {"Damage": 10},
                          "trait": "Fire Affinity"},

                         {"name": "Shadowfang",
                          "description": "imbued with the essence of darkness, allowing it to strike fear into the hearts of enemies.",
                          "bonus": {"Damage": 15},
                          "trait": "Stealth Enhancement"},

                         {"name": "Stormbreaker",
                          "description": "imbued with the power of storms, causing it to vibrate with electricity.",
                          "bonus": {"Damage": 10, "Defense": 15},
                          "trait": "Lightning Affinity"},

                         {"name": "Frostwood",
                          "description": "carved from the heart of an ancient glacier, providing insulation and strength.",
                          "bonus": {"Defense": 20},
                          "trait": "Ice Affinity"},

                         {"name": "Stoneheart",
                          "description": "crafted from the hardest stone, making it incredibly durable and resistant to damage.",
                          "bonus": {"Defense": 5, "Durability": 15},
                          "trait": None},

                         {"name": "Blazing",
                          "description": "enchanted with the essence of fire, causing it to emit intense heat and flames.",
                          "bonus":{},
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


# View an expanded description of the item
def ViewDescription(name, lootCategory, rarity, stat, statType, durability, trait, description):
    GeneratedLootHeader()
    print(f"Name: {name}")
    print(f"Type: {lootCategory}")
    print(f"Rarity: {rarity}\n")

    print(f"{statType}: {stat}")
    print(f"Durability: {durability}\n")

    print("\nDescription:")
    print(textwrap.fill(description, width=45))
    if trait:
        print(trait)

    print("\nPress enter to return...", end='')
    input()


# Function to display the loot options menu
def LootOptions(saved):
    savedMessage = " (Already Saved)" if saved else ""

    print("\n--------------------------------------------\n")

    print("   1. View Description")
    print(f"   2. Save Item{savedMessage}")
    print("   3. Generate Another (Same Chosen Category)")
    print("   4. Choose Another Category")
    print("   5. Return to Main Menu\n")

    print("Select an option (1-5): ", end="")


# Function to generate random loot based on the selected category
def GenerateLoot(category):
    rarity = random.choice(RARITIES)

    # Determine the type and stat type based on the category
    if category == "Weapon":
        types = ["Sword", "Axe", "Bow", "Dagger"]
        statType = "Damage"
    elif category == "Armor":
        types = ["Helmet", "Chestplate", "Leggings", "Boots"]
        statType = "Defense"
    else:  # Accessory
        types = ["Ring", "Amulet", "Bracelet"]
        statType = random.choice(["Damage", "Defense"])

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

    # Generate the base stats for the loot item
    itemType = random.choice(types)
    stat = int(random.randint(50, 100) * statModifier)
    durability = int(random.randint(50, 100) * statModifier)

    # Determine the appropriate article ("A" or "An") based on the first letter of the item type, or none if plural
    article = "An " if itemType[0].lower() in "aeiou" else "A "
    article = "" if itemType[-1].lower() == "s" else article

    # If the rarity is Epic or Legendary, use the modifier's name and description, and apply bonus stats
    if rarity in ["Epic", "Legendary"]:
        name = f"{modifier['name']} {itemType}"
        traits = []

        # Apply bonus stats from the modifier to the base stats
        for modName, modValue in modifier["bonus"].items():
            if modName == "Durability":
                durability += modValue
                traits.append(f"Durability +{modValue}")

            elif modName == statType:
                stat += modValue
                traits.append(f"{modName} +{modValue}")

        # Generate the description and trait based on the modifier
        itemType = itemType.lower() if itemType[-1].lower() != "s" else itemType
        description = f"{article}{itemType} {modifier['description']}"

        if modifier["trait"]:
            traits.append(modifier["trait"])

        # Format the traits into a single string, or set to None if there are no traits
        trait = ", ".join(traits) if traits else None
        trait = f"{modifier['name']}: {trait}" if trait else None

    # If the rarity is Common, Uncommon, or Rare, generate the apropriate name and description based on the modifier
    else:
        name = f"{modifier} {itemType}"
        trait = None
        if rarity in ["Uncommon", "Rare"]:
            itemType = itemType.lower() if itemType[-1].lower() != "s" else itemType
            description = f"{article}{itemType} forged from {modifier}."
        else: # Common
            article = "An " if modifier.lower() in "aeiou" else "A "
            article = "" if itemType[-1].lower() == "s" else article
            modifier = modifier.lower() if itemType[-1].lower() != "s" else modifier
            description = f"{article}{modifier} {itemType.lower()}, barely usable."

    return name, rarity, statType, stat, description, durability, trait


def LootMenu(category):
    choice = 0
    saved = False
    lootCategory = random.choice(CATEGORIES) if category == "Random" else category

    GeneratedLootHeader() # Display the generated loot header
    name, rarity, statType, stat, description, durability, trait = GenerateLoot(lootCategory)
    LootSummary(name, lootCategory, rarity, stat, statType, durability, trait)

    while choice not in (4, 5):
        LootOptions(saved) # Display the loot options menu

        # Get user input for the loot options choice and handle invalid input
        try:
            choice = int(input())
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 5.")
            continue

        match choice:
            case 1: # View description
                ViewDescription(name, lootCategory, rarity, stat, statType, durability, trait, description)

            case 2: # Save item
                SaveLoot(name, lootCategory, rarity, stat, statType, durability, trait, description)
                print(f"\nItem '{name}' saved!\n")
                saved = True

            case 3: # Generate another
                lootCategory = random.choice(CATEGORIES) if category == "Random" else category

                name, rarity, statType, stat, description, durability, trait = GenerateLoot(lootCategory)
                LootSummary(name, lootCategory, rarity, stat, statType, durability, trait)
                saved = False

            case 4: # Return to categories menu
                return "Category"

            case 5: # Return to Main Menu
                MainMenuHeader() # Display the main menu header again after returning from loot menu
                return "Main"

            case _: # Handle invalid loot option choice
                print("\nInvalid choice. Please select a valid option.")

    


def SaveLoot(name, category, rarity, stat, statType, durability, trait, description):
    filename = "saved_loot.json"

    # Load existing loot, or create an empty list
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                loot = json.load(file)
            except json.JSONDecodeError:
                loot = []
    else:
        loot = []

    # Create a dictionary for the new item
    newLoot = {
        "name": name,
        "category": category,
        "rarity": rarity,
        "stat": stat,
        "statType": statType,
        "durability": durability,
        "trait": trait,
        "description": description
    }

    # Add the item and save the updated list
    loot.append(newLoot)

    with open(filename, "w") as file:
        json.dump(loot, file, indent=4)


# Main function to run the loot generator program
def main():
    mainMenuChoice = 0

    MainMenuHeader() # Display the main menu header

    # Loop to keep the program running until the user chooses to exit
    while mainMenuChoice != 3:
        MainMenu() # Display the main menu options
        menuReturn = ""

        # Get user input for the main menu choice and handle invalid input
        try:
            mainMenuChoice = int(input())
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 3.")
            continue

        match mainMenuChoice:
            case 1: # Choose a category
                categoryChoice = 0

                while categoryChoice != 5:
                    ChooseCategory()

                    try:
                        categoryChoice = int(input())
                    except ValueError:
                        print("\nInvalid input. Please enter a number between 1 and 5.")
                        continue

                    match categoryChoice:
                        case 1:
                            menuReturn = LootMenu("Weapon")
                        case 2:
                            menuReturn = LootMenu("Armor")
                        case 3:
                            menuReturn = LootMenu("Accessory")
                        case 4:
                            menuReturn = LootMenu("Random")
                        case 5:
                            pass
                        case _:
                            print("\nInvalid choice. Please select a valid option.")

            case 2: # Generate random loot
                menuReturn = LootMenu("Random")
                if menuReturn == "Category":
                    CategoryMenu()

            case 3: # Exit the program
                pass

            case _: # Handle invalid menu choice
                print("\nInvalid choice. Please select a valid option.")

    print("\nThank you for using this loot generator. Goodbye!\n")
        

# Entry point of the program
if __name__ == "__main__":
    main()