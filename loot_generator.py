

def MainMenu():
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

    print("\n--------------------------------------------\n")

    print("   1. Choose a Category")
    print("   2. Generate Random Loot")
    print("   3. Exit\n")

    print("Select an option (1-3): ")

def ChooseCategory():
    print("\n--------------------------------------------\n")

    print("Choose a loot category to generate, or Random")
    print("to let the generator choose for you.\n")

    print("   1. Weapon")
    print("   2. Armor")
    print("   3. Accessory")
    print("   4. Random")
    print("   5. Return to Main Menu\n")

    print("Select an option (1-5): ")

def GeneratedLootHeader():
    print("\n--------------------------------------------\n")
    print("               Generated Loot")
    print("\n--------------------------------------------\n")

def GeneratedLoot(name, type, rarity, stat, statType, durability, trait = None):
    print(f"Name: {name}")
    print(f"Type: {type}")
    print(f"Rarity: {rarity}\n")

    print(f"{statType}: {stat}")
    print(f"Durability: {durability}")
    if trait:
        print(f"Trait: {trait}")



def main():
    MainMenu()
    ChooseCategory()
    GeneratedLootHeader()
    
if __name__ == "__main__":
    main()