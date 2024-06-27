import csv
def bake_cookies(filepath):

    cookies = []
    with open(filepath, mode='r') as c_file:
        reader = csv.DictReader(c_file)
        for row in reader:
            cookie = {
                'id': int(row['id']),
                'title': row['name'],
                'description': row['description'],
                'price': float(row['price'].strip('$')),
                'sugar_free': 'sugar' not in row['ingredients'].lower(),
                'gluten_free': 'gluten' not in row['ingredients'].lower(),
                'contains_nuts': 'nuts' in row['ingredients'].lower()
            }
            cookies.append(cookie)
    return cookies

def welcome():
    # write your code for this function below this line
    print("Welcome to the Python Cookie Shop!\nWe feed each according to their need.\n")

    print("We'd hate to trigger an allergic reaction in your body. So please answer the following questions:")
    sugar_free = input("Do you suffer from diabetes? (yes/y): ").strip().lower() in ['yes', 'y']
    gluten_free = input("Are you allergic to gluten? (yes/y): ").strip().lower() in ['yes', 'y']
    contains_nuts = input("Are you allergic to nuts? (yes/y): ").strip().lower() in ['yes', 'y']

    return sugar_free, gluten_free, contains_nuts


def display_cookies(cookies,allergies=None):
    # write your code for this function below this line
    if allergies is None:
        allergies = {'sugar_free': False, 'gluten_free': False, 'contains_nuts': False}

    print("\nGreat! Here are the cookies that match your dietary needs:\n")

    for cookie in cookies:
        if (allergies['sugar_free'] and not cookie['sugar_free']) or \
           (allergies['gluten_free'] and not cookie['gluten_free']) or \
           (allergies['contains_nuts'] and cookie['contains_nuts']):
            continue

        print(f"  #{cookie['id']} - {cookie['title']}")
        print(f"  {cookie['description']}")
        print(f"  Price: ${cookie['price']:.2f}\n")



def get_cookie_from_dict(id, cookies):
    for cookie in cookies:
        if cookie.get('id') == id:
            return cookie
    return None

def solicit_quantity(id, cookies):
    cookie = get_cookie_from_dict(id, cookies)
    if cookie:
        while True:
            try:
                quantity = int(input(f"My favorite! How many {cookie['title']} would you like? "))
                if quantity > 0:
                    subtotal = quantity * cookie['price']
                    print(f"Your subtotal for {quantity} {cookie['title']} is ${subtotal:.2f}.")
                    return quantity
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def solicit_order(cookies):
    # write your code for this function below this line
    orders = []
    while True:
        user_orders = input('Please enter the number of any cookie you would like to purchase (type "finished" if done): ').strip().lower()
        if user_orders in ['finished', 'done', 'quit', 'exit']:
            break
        try:
            id = int(user_orders)
            cookie = get_cookie_from_dict(id, cookies)
            if cookie:
                quantity = solicit_quantity(id, cookies)
                orders.append({'id': id, 'quantity': quantity})
            else:
                print("Sorry, we don't have a cookie with that id. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'finished' to complete your order.")
    return orders

def display_order_total(order, cookies):
    # write your code for this function below this line
    order_details = {}
    total_cost = 0

    for item in order:
        cookie = get_cookie_from_dict(item['id'], cookies)
        if cookie:
            title = cookie['title']
            quantity = item['quantity']
            cost = cookie['price'] * quantity
            total_cost += cost
            if title in order_details:
                order_details[title] += quantity
            else:
                order_details[title] = quantity

    print("Thank you for your order. You have ordered:\n")
    for title, quantity in order_details.items():
        print(f"-{quantity} {title}")
    print(f"\nYour total is ${total_cost:.2f}.")
    print("Please pay with Bitcoin before picking-up.\n")
    print("Thank you!")
    print("-The Python Cookie Shop Robot.")

def run_shop(cookies):
    # write your code for this function below here.
    welcome()
    display_cookies(cookies,allergies=None)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
