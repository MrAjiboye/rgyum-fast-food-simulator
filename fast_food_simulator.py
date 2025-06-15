import pandas as pd

def load_and_clean_data():
    """Load and preprocess menu and foods CSV files."""
    # Load data
    menu = pd.read_csv('https://www.dropbox.com/s/aer7yfyzrd6yog5/menu.csv?raw=1')
    foods = pd.read_csv('https://www.dropbox.com/s/ln97rid8o3bdh1h/foods.csv?raw=1')
    
    # Standardize food names in foods DataFrame
    def change_name(x):
        words = x.split()
        if len(words) == 1:
            return x.capitalize()
        elif len(words) == 2:
            return words[1].capitalize()
        else:
            return f"{words[-2].capitalize()} {words[-1].capitalize()}"
    
    foods.at[6, 'food'] = 'Yakisoba'  # Specific fix for Yakisoba
    foods['food'] = foods['food'].apply(change_name)
    
    # Merge datasets
    menu_food = pd.merge(menu, foods, how='left').set_index('menu_number')
    
    # Add Chips to B4
    menu_food.loc['B4'] = ['Chips', 3.0, 'side', 3.00]
    
    return menu_food

def admin_login(attempts_left, max_attempts=4):
    """Handle admin login with username and password validation."""
    username = input("\nPlease enter your username: ")
    if username != 'admin':
        print(f"Invalid username. {attempts_left - 1} attempts left.")
        return False, attempts_left - 1
    
    try:
        password = float(input("Please enter your password (number < 10): "))
        if password < 10:
            print("\033[1mLogin successful!\033[0m")
            return True, attempts_left
        else:
            print(f"Incorrect password. {attempts_left - 1} attempts left.")
            return False, attempts_left - 1
    except ValueError:
        print(f"Invalid password (must be a number). {attempts_left - 1} attempts left.")
        return False, attempts_left - 1

def add_product(menu_food, admin_logged_in):
    """Add one product to a non-empty menu slot (admin only)."""
    if not admin_logged_in:
        print("Login first!")
        return
    
    print("\nCurrent menu:")
    print(menu_food.to_string(index=True))
    menu_num = input("\nEnter menu number to add product (e.g., A1): ").upper()
    
    if menu_num not in menu_food.index:
        print("Invalid menu number.")
        return
    if pd.isna(menu_food.loc[menu_num, 'food']) or pd.isna(menu_food.loc[menu_num, 'amount']):
        print("Cannot add products to an empty menu slot.")
        return
    if menu_food.loc[menu_num, 'amount'] >= 8:
        print(f"Cannot add more {menu_food.loc[menu_num, 'food']}. Menu slot is full (max 8).")
        return
    
    menu_food.loc[menu_num, 'amount'] += 1
    print(f"One more {menu_food.loc[menu_num, 'food']} added to {menu_num}.")

def buy_product(menu_food):
    """Handle product purchase with payment processing."""
    print("\nCurrent menu:")
    print(menu_food.to_string(index=True))
    menu_num = input("Enter menu number to buy product (e.g., B1): ").upper()
    
    if menu_num not in menu_food.index:
        print("Invalid menu number.")
        return
    if pd.isna(menu_food.loc[menu_num, 'food']) or pd.isna(menu_food.loc[menu_num, 'amount']):
        print("This menu slot is empty.")
        return
    if menu_food.loc[menu_num, 'amount'] == 0:
        print(f"Sorry, no {menu_food.loc[menu_num, 'food']} left.")
        return
    
    price = menu_food.loc[menu_num, 'price']
    print(f"The price of {menu_food.loc[menu_num, 'food']} is £{price:.2f}.")
    
    total_payment = 0
    while total_payment < price:
        try:
            payment = float(input("Enter payment amount: "))
            if payment <= 0:
                print("Payment must be a positive number.")
                continue
            total_payment += payment
            if total_payment < price:
                print(f"You need to pay £{(price - total_payment):.2f} more.")
        except ValueError:
            print("Invalid payment amount. Please enter a number.")
    
    if total_payment > price:
        print(f"Your change is £{(total_payment - price):.2f}.")
    else:
        print("Thanks for paying!")
    
    menu_food.loc[menu_num, 'amount'] -= 1
    print(f"There are now {menu_food.loc[menu_num, 'amount']} {menu_food.loc[menu_num, 'food']} left.")

def main():
    """Run the fast-food simulation program."""
    menu_food = load_and_clean_data()
    loop = True
    admin_logged_in = False
    attempts_left = 4
    
    while loop and attempts_left > 0:
        print("\nWelcome to the RGyUm Fast-Food Menu")
        print("1. Log in (admin only)")
        print("2. Add one more product (admin only)")
        print("3. Buy products")
        print("4. Exit")
        
        option = input(">> ").strip()
        
        if option not in ['1', '2', '3', '4']:
            print("Invalid option. Please select 1, 2, 3, or 4.")
            continue
        
        if option == '1':
            if admin_logged_in:
                print("You are already logged in as admin.")
                continue
            admin_logged_in, attempts_left = admin_login(attempts_left)
            if attempts_left == 0:
                print("Maximum login attempts reached. Exiting program...")
                loop = False
            continue
        
        if option == '2':
            add_product(menu_food, admin_logged_in)
            continue
        
        if option == '3':
            buy_product(menu_food)
            continue
        
        if option == '4':
            print("Exiting the program...")
            loop = False

if __name__ == "__main__":
    main()