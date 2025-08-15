# 🍽️ Restaurant Menu Order System

This is a simple menu order system presented to the user. On the system (or app), the user is presented with a menu and is allowed to choose items on the menu. The menu includes prices.

*I am assumming that you already have python installed in your system or computer. So I won't cover the steps involved in installing python hereon.*

## 📋 Project Overview

This interactive command-line (CLI) application allows customers to:
- View a restaurant menu with South African Rand (ZAR) pricing
- Select multiple items with specified quantities
- View an itemized order summary with total cost
- Visualize their order with charts and graphs
- Save their order receipt to a text file

## 🎯 Learning Objectives

The project is based on the chapters learnt on the Python Programming class offered by *Mentec*. Below are the chapters covered on the course:
- **Chapter 1:** Introduction to Python
- **Chapter 2:** Variables and Data Types
- **Chapter 3:** User Input and Output
- **Chapter 4:** Conditional Statements
- **Chapter 5:** Loops
- **Chapter 6:** Functions
- **Chapter 7:** Lists and Tuples
- **Chapter 8:** Dictionaries and Sets
- **Chapter 9:** File Handling
- **Chapter 10:** Error Handling and Debugging
- **Chapter 11:** Object-Oriented Programming (OOP)
- **Chapter 12:** Working with Modules and Libraries
- **Chapter 13:** Introduction to APIs and JSON
- **Chapter 14:** Intro to Data Visualization (Optional)

## 🚀 Features

### Core Functionality
- **Interactive Menu Display**: Shows all available items with prices in South African Rands (ZAR)
- **Order Management**: Add multiple items with custom quantities
- **Input Validation**: Prevents invalid menu selections and quantity entries
- **Order Summary**: Detailed receipt with itemized costs and total
- **Real-time Calculations**: Automatic total calculation as items are added

### Advanced Features
- **Data Visualization**: 
  - Bar chart showing quantity of each item ordered
  - Pie chart displaying order value distribution
- **File Export**: Save order receipts as timestamped text files
- **Error Handling**: Comprehensive error management for user mistakes
- **Professional Formatting**: Clean, readable output with emojis and formatting
- 

## 🎮 How to Use the System (or App)

### Step-by-Step Usage

1. **Start the Program**
   ```
   python main.py
   ```

2. **Enter Your Name**
   - The system will prompt for your name
   - This personalizes your order experience

3. **View the Menu**
   ```
   🍽️  RESTAURANT MENU 🍽️
   ==============================
   Burger     - R65.00
   Pizza      - R89.50
   Chicken    - R75.00
   Salad      - R45.00
   Chips      - R25.00
   Drink      - R15.00
   Dessert    - R35.00
   ==============================
   ```

4. **Place Your Order**
   - Type the item name (e.g., "burger", "pizza")
   - Enter the quantity you want
   - Continue adding items or type "done" to finish

5. **Review Your Order**
   - View the complete order summary
   - See the total cost calculation

6. **Optional Features**
   - Choose to view order visualization charts
   - Save your receipt to a text file

### Sample Interaction
```
🎉 Welcome to Our Restaurant! 🎉

Enter your name: Mongadi

Hello Mongadi! Let's take your order.

🍽️  RESTAURANT MENU 🍽️
==============================
Burger     - R65.00
Pizza      - R89.50
...

Enter item name (or 'done' to finish): burger
How many burger(s)? 2
✅ Added 2 x Burger to your order!

Enter item name (or 'done' to finish): drink
How many drink(s)? 2
✅ Added 2 x Drink to your order!

Enter item name (or 'done' to finish): done

--- Order Summary for Mongadi ---
Order Time: 2024-08-14 10:30:45
----------------------------------------
Burger: 2 x R65.00 = R130.00
Drink: 2 x R15.00 = R30.00
----------------------------------------
Total: R160.00
```

## 📊 Menu Items & Pricing

| Item | Price (ZAR) | Description |
|------|-------------|-------------|
| Burger | R65.00 | Classic beef burger |
| Pizza | R89.50 | Margherita pizza |
| Chicken | R75.00 | Grilled chicken breast |
| Salad | R45.00 | Fresh garden salad |
| Chips | R25.00 | Crispy potato chips |
| Drink | R15.00 | Soft drinks/beverages |
| Dessert | R35.00 | Daily dessert special |

*Prices are in South African Rands (ZAR)*

## 📈 Visualization Features

The system generates two types of charts:

1. **Bar Chart**: Shows the quantity of each item ordered
   - X-axis: Menu items
   - Y-axis: Quantity ordered
   - Includes value labels on each bar

2. **Pie Chart**: Displays the monetary value distribution
   - Shows percentage of total order value per item
   - Includes rand amounts in labels
   - Color-coded for easy interpretation

## 💾 File Output

Order receipts are automatically saved with the format:
```
order_[CustomerName]_[YYYYMMDD_HHMMSS].txt
```

Example filename: `order_Mongadi_20240814_094243.txt`

Sample receipt content:
```
RESTAURANT ORDER RECEIPT
========================
Customer: Mongadi
Date & Time: 2024-08-14 10:30:45
------------------------
Burger: 2 x R65.00 = R130.00
Drink: 2 x R15.00 = R30.00
------------------------
TOTAL: R160.00
========================
Thank you for your order!
```

## 🐛 Error Handling

The system handles various error scenarios:

- **Invalid Menu Items**: Prevents ordering items not on the menu
- **Invalid Quantities**: Ensures positive integer quantities
- **Empty Names**: Requires valid customer name input
- **File Errors**: Graceful handling of file save failures
- **Keyboard Interruption**: Clean exit with Ctrl+C
- **Input Type Errors**: Validates numeric input for quantities

## 📝 License

This project is created for educational purposes and is free to use, modify, and distribute for learning and teaching Python programming.

---
