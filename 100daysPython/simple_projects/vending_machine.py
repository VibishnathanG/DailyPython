import time
from typing import Dict, Optional

class VendingMachine:
    # Constants
    ADMIN_PASSWORD = "admin123"
    PRICES = {"coffee": 20, "tea": 20, "milk": 20}
    RECIPES = {
        "coffee": {"coffee_powder": 10, "sugar": 10, "milk": 20, "water": 20},
        "tea": {"tea_powder": 10, "sugar": 10, "milk": 20, "water": 20},
        "milk": {"milk": 100, "sugar": 10}
    }
    
    def __init__(self):
        self.inventory = {
            "coffee_powder": 100,
            "sugar": 200,
            "milk": 500,
            "water": 1000,
            "tea_powder": 100,
            "money": 0
        }
        self.is_operational = True
    
    def check_ingredients(self, drink: str) -> bool:
        """Check if enough ingredients are available for the drink"""
        recipe = self.RECIPES[drink]
        for ingredient, amount in recipe.items():
            if self.inventory.get(ingredient, 0) < amount:
                return False
        return True
    
    def update_inventory(self, drink: str):
        """Update inventory after making a drink"""
        recipe = self.RECIPES[drink]
        for ingredient, amount in recipe.items():
            self.inventory[ingredient] -= amount
        self.inventory["money"] += self.PRICES[drink]
    
    def get_payment(self, drink: str) -> Optional[int]:
        """Get payment from user with validation"""
        price = self.PRICES[drink]
        try:
            amounts_input = input(f"{drink.title()} costs ${price}. Enter amounts separated by spaces: ")
            amounts = list(map(int, amounts_input.split()))
            total = sum(amounts)
            
            if total < price:
                print(f"Insufficient payment. Need ${price - total} more.")
                return None
            return total
        except ValueError:
            print("Invalid payment format. Please enter numbers only.")
            return None
    
    def make_drink(self, drink: str) -> bool:
        """Make a drink if ingredients are available"""
        if not self.check_ingredients(drink):
            print("Sorry, not enough ingredients available.")
            self.shutdown_for_maintenance()
            return False
        
        payment = self.get_payment(drink)
        if payment is None:
            return False
        
        self.update_inventory(drink)
        change = payment - self.PRICES[drink]
        print(f"Enjoy your {drink}! Your change: ${change}")
        return True
    
    def shutdown_for_maintenance(self):
        """Shutdown machine for maintenance"""
        print("Machine out of order. Calling admin for maintenance.")
        time.sleep(1)
        self.is_operational = False
    
    def authenticate_admin(self) -> bool:
        """Authenticate admin user"""
        try:
            password = input("Enter admin password: ")
            return password == self.ADMIN_PASSWORD
        except KeyboardInterrupt:
            return False
    
    def show_report(self):
        """Display inventory report"""
        print("\n=== INVENTORY REPORT ===")
        for item, quantity in self.inventory.items():
            print(f"{item.replace('_', ' ').title()}: {quantity}")
        print("========================\n")
    
    def reset_inventory(self):
        """Reset inventory to default values"""
        self.inventory = {
            "coffee_powder": 100,
            "sugar": 200,
            "milk": 500,
            "water": 1000,
            "tea_powder": 100,
            "money": 0
        }
        print("Inventory reset successfully!")
    
    def admin_menu(self):
        """Handle admin operations"""
        if not self.authenticate_admin():
            print("Authentication failed!")
            return
        
        while True:
            try:
                print("\n=== ADMIN MENU ===")
                print("1. View Report")
                print("2. Shutdown Machine")
                print("3. Reset Inventory")
                print("4. Start Machine")
                print("5. Exit Admin")
                
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    self.show_report()
                elif choice == 2:
                    self.is_operational = False
                    print("Machine shutdown initiated.")
                    break
                elif choice == 3:
                    self.reset_inventory()
                elif choice == 4:
                    self.is_operational = True
                    print("Machine started successfully!")
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Please try again.")
                    
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def customer_menu(self):
        """Handle customer operations"""
        try:
            print("\n=== DRINK MENU ===")
            print("1. Coffee - $20")
            print("2. Tea - $20")
            print("3. Milk - $20")
            
            choice = int(input("Your choice: "))
            
            if choice == 1:
                self.make_drink("coffee")
            elif choice == 2:
                self.make_drink("tea")
            elif choice == 3:
                self.make_drink("milk")
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def run(self):
        """Main machine operation loop"""
        print("Welcome to Vibish Vending Machine!")
        
        while self.is_operational:
            try:
                print("\n=== MAIN MENU ===")
                print("1. Customer")
                print("2. Admin")
                print("3. Exit")
                
                user_type = int(input("Select user type: "))
                
                if user_type == 1:
                    self.customer_menu()
                elif user_type == 2:
                    self.admin_menu()
                elif user_type == 3:
                    print("Thank you for using Vibish Vending Machine!")
                    break
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
                    
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\nShutting down machine...")
                break
        
        print("Machine is now offline.")

# Run the vending machine
if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()