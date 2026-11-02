import random


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


def MainMenu():
    print("\n--------------------------------------------\n")
    
    print("   1. Choose a Category")
    print("   2. Generate Random Loot")
    print("   3. Exit\n")
    
    print("Select an option (1-3): ", end="")


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


def GeneratedLootHeader():
    print("\n--------------------------------------------\n")
    print("               Generated Loot")
    print("\n--------------------------------------------\n")


def GeneratedLoot(name, type, rarity, stat, statType, durability, trait):
    print(f"Name: {name}")
    print(f"Type: {type}")
    print(f"Rarity: {rarity}\n")

    print(f"{statType}: {stat}")
    print(f"Durability: {durability}")
    if trait:
        print(f"Trait: {trait}")


def main():
    mainMenuChoice = 0
    categoryChoice = 0

    MainMenuHeader()
    while mainMenuChoice != 3:
        MainMenu()

        try:
            mainMenuChoice = int(input())
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 3.")
            continue

        match mainMenuChoice:
            case 1:
                # Choose a category logic here
                pass
            case 2:
                # Generate random loot logic here
                pass
            case 3:
                pass  # Exit the loop and end the program
            case _:
                print("\nInvalid choice. Please select a valid option.")

    print("\nThank you for using this loot generator. Goodbye!")
        
    
if __name__ == "__main__":
    main()