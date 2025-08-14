# Restaurant Menu Order System - Foodhub

# Import necessary libraries
import matplotlib.pyplot as plt
from datetime import datetime

# Create a simple menu as a dictionary
menu = {
    "burger": 65.00,
    "pizza": 89.50,
    "chicken": 75.00,
    "salad": 45.00,
    "chips": 25.00,
    "drink": 15.00,
    "dessert": 35.00
}

# Create a class to represent an order
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}  
        self.order_time = datetime.now() 
    
    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
    
# Function to calculate the total order value
    def calculate_total(self):
        total = 0
        for item, quantity in self.items.items():
            total += menu[item] * quantity
        return total
    
# Function to display the order summary
    def display_order(self):
        print(f"\n--- Order Summary for {self.customer_name} ---")
        print(f"Order Time: {self.order_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)
        
        for item, quantity in self.items.items():
            item_total = menu[item] * quantity
            print(f"{item.title()}: {quantity} x R{menu[item]:.2f} = R{item_total:.2f}")
        
        print("-" * 40)
        print(f"Total: R{self.calculate_total():.2f}")

# Function to display the menu
def display_menu():
    print("\n🍽️  RESTAURANT MENU 🍽️")
    print("=" * 30)
    for item, price in menu.items():
        print(f"{item.title():<10} - R{price:.2f}")
    print("=" * 30)

# Function for getting user input
def get_customer_name():
    
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Please enter a valid name!")

# Obtain the user order.
def take_order():
    customer_name = get_customer_name()
    order = Order(customer_name)
    
    print(f"\nHello {customer_name}! Let's take your order.")
    
    # Create a loop for taking orders and wait for the user to finish.
    while True:
        display_menu()
        
        try:
            item = input("\nEnter item name (or 'done' to finish): ").lower().strip()
            
            if item == 'done':
                break
            elif item not in menu:
                print("❌ Item not available! Please choose from the menu.")
                continue
            
            quantity = int(input(f"How many {item}(s)? "))
            
            if quantity <= 0:
                print("❌ Quantity must be greater than 0!")
                continue
            
            order.add_item(item, quantity)
            print(f"✅ Added {quantity} x {item.title()} to your order!")
            
        except ValueError:
            print("❌ Please enter a valid number for quantity!")
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    
    return order

# Start data visualization
def create_order_chart(order):
    if not order.items:
        print("No items to visualize!")
        return
    
    # Prepare data for visualization spit this to the list
    items = list(order.items.keys())
    quantities = list(order.items.values())
    
    # Create bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(items, quantities, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF'])
    
    plt.title(f"Order Summary for {order.customer_name}", fontsize=16, fontweight='bold')
    plt.xlabel('Menu Items', fontsize=12)
    plt.ylabel('Quantity Ordered', fontsize=12)
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for bar, quantity in zip(bars, quantities):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                str(quantity), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Create pie chart for order value distribution
    item_totals = []
    labels = []
    
    for item, quantity in order.items.items():
        total_value = menu[item] * quantity
        item_totals.append(total_value)
        labels.append(f"{item.title()}\nR{total_value:.2f}")
    
    plt.figure(figsize=(8, 8))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF']
    plt.pie(item_totals, labels=labels, autopct='%1.1f%%', colors=colors[:len(item_totals)], startangle=90)
    plt.title(f"Order Value Distribution - Total: R{order.calculate_total():.2f}", 
              fontsize=14, fontweight='bold')
    plt.show()

# Handle files
def save_order_to_file(order):
    
    try:
        filename = f"order_{order.customer_name}_{order.order_time.strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Display the menu to the user
        with open(filename, 'w') as file:
            file.write(f"RESTAURANT ORDER RECEIPT\n")
            file.write(f"========================\n")
            file.write(f"Customer: {order.customer_name}\n")
            file.write(f"Date & Time: {order.order_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"------------------------\n")
            
            for item, quantity in order.items.items():
                item_total = menu[item] * quantity
                file.write(f"{item.title()}: {quantity} x R{menu[item]:.2f} = R{item_total:.2f}\n")
            
            # Show the user items on the order with amounts
            file.write(f"------------------------\n")
            file.write(f"TOTAL: R{order.calculate_total():.2f}\n")
            file.write(f"========================\n")
            file.write("Thank you for your order!\n")
        
        print(f"✅ Order saved to {filename}")
        
    except Exception as e:
        print(f"❌ Error saving order: {e}")

# Main program
def main():
    print("🎉 Welcome to Our Restaurant! 🎉")
    
    try:
        # Take the order
        order = take_order()
        
        # Check if any items were ordered
        if not order.items:
            print("No items ordered. Come back soon! 👋")
            return
        
        # Display order summary
        order.display_order()
        
        # Ask if user wants to see visualizations
        show_chart = input("\nWould you like to see your order chart? (yes/no): ").lower().strip()
        if show_chart in ['yes', 'y']:
            create_order_chart(order)
        
        # Ask if user wants to save order
        save_order = input("Would you like to save your order receipt? (yes/no): ").lower().strip()
        if save_order in ['yes', 'y']:
            save_order_to_file(order)
        
        print(f"\nThank you for ordering, {order.customer_name}! 🍴")
        print("Your order will be ready shortly! ⏰")
        
    except KeyboardInterrupt:
        print("\n\nOrder cancelled. Thank you for visiting! 👋")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()