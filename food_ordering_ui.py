#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Solomon diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  print(functions.get_item_information(item_code))

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)


def show_manager_menu():
    while True:
        print("\nManager Options")
        print("1. Add a new menu item")
        print("2. Remove a menu item")
        print("3. Update a menu item (Price or Description)")
        print("4. View menu")
        print("Q. Quit to main menu")
        
        manager_choice = input("Your choice: ").upper()
        
        if manager_choice == '1':
            add_menu_item()
        elif manager_choice == '2':
            remove_menu_item()
        elif manager_choice == '3':
            update_menu_item()
        elif manager_choice == '4':
            view_menu()
        elif manager_choice == 'Q':
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or Q.")

def add_menu_item():
    code = input("Enter item code (e.g., E5): ").upper()
    name = input("Enter item name (e.g., PIZZA): ").upper().replace(" ", "_")
    price = float(input("Enter item price: "))
    stock = int(input("Enter item stock: "))
    
    # Add the new item to the menu_items_dict
    new_item = {
        'code': code,
        'name': name,
        'price': price,
        'stock': stock
    }
    
    data.menu_items_dict.append(new_item)
    print(f"Item {name} added to the menu.")

def remove_menu_item():
    code = input("Enter the item code to remove (e.g., E1): ").upper()
    
    # Remove the item from the menu_items_dict
    for item in data.menu_items_dict:
        if item['code'] == code:
            data.menu_items_dict.remove(item)
            print(f"Item {item['name']} removed from the menu.")
            return
    
    print("Item code not found.")

def update_menu_item():
    code = input("Enter the item code to update (e.g., E1): ").upper()
    
    # Find the item in the menu and update its information
    for item in data.menu_items_dict:
        if item['code'] == code:
            print(f"Current details: Name: {item['name']}, Price: {item['price']}, Stock: {item.get('stock', 'Unlimited')}")
            choice = input("Do you want to update Price (P), Description (D), or both (B)? ").upper()
            
            if choice in ['P', 'B']:
                new_price = float(input(f"Enter new price for {item['name']}: "))
                item['price'] = new_price
                print(f"Price updated to {new_price}.")
                
            if choice in ['D', 'B']:
                new_name = input(f"Enter new description for {item['name']}: ").upper().replace(" ", "_")
                item['name'] = new_name
                print(f"Description updated to {new_name}.")
            
            return
    
    print("Item code not found.")

def view_menu():
    print("\nCurrent Menu:")
    for item in data.menu_items_dict:
        stock_info = item.get('stock', 'Unlimited')
        print(f"Code: {item['code']}, Name: {item['name']}, Price: ${item['price']:.2f}, Stock: {stock_info}")
    print("\n")
if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()


