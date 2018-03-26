"""
command line menu program
"""

from uuid import uuid4
import csv

intro = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**************************************
'''

order_prompt = '''
**********************************************************************
** What would you like to order?                                    **
** To add an item to your order, type the item name                 **
** To see the menu, type "menu"                                     **
** To order from togo menu, type "togo"                             **
** To remove an item from your order, type the "remove <item name>" **
** To see your current order, type "order"                          **
** To checkout and pay, type "checkout"                             **
** To quit at any time, type "quit"                                 **
**********************************************************************
\n'''

full_menu = {
    'Appetizers': {
        'Wings': [0, 2.00, 10],
        'Calamari': [0, 2.00, 10],
        'Spring Rolls': [0, 2.00, 10],
        'Nachos': [0, 2.00, 10],
        'Spinach Dip': [0, 2.00, 10],
        'Sampler': [0, 2.00, 10],
        'Mozz Sticks': [0, 2.00, 10],
        'Corn Doggies': [0, 2.00, 10],
        'Hummus': [0, 2.00, 10],
        'Almonds': [0, 2.00, 10],
        'Chips': [0, 2.00, 10],
        'Oreos': [0, 2.00, 10]
    },
    'Entrees': {
        'Salmon': [0, 10.00, 10],
        'Steak': [0, 10.00, 10],
        'Tacos': [0, 10.00, 10],
        'Salad': [0, 10.00, 10],
        'Pizza': [0, 10.00, 10],
        'Vegetarian Delight': [0, 10.00, 10],
        'Pasta': [0, 10.00, 10],
        'Ribs': [0, 10.00, 10],
        'Burrito': [0, 10.00, 10],
        'Grilled Chicken': [0, 10.00, 10],
        'Fried Fish': [0, 10.00, 10],
        'S\'ghetti': [0, 10.00, 10]
    },
    'Sides': {
        'French Fries': [0, 4.00, 10],
        'Hush Puppies': [0, 4.00, 10],
        'Green Beans': [0, 4.00, 10],
        'Mashed Potatoes': [0, 4.00, 10],
        'Corn': [0, 4.00, 10],
        'Rolls': [0, 4.00, 10],
        'Carrots': [0, 4.00, 10],
        'Biscuits': [0, 4.00, 10],
        'Mac and Cheese': [0, 4.00, 10],
        'Spinach': [0, 4.00, 10],
        'Asparagus': [0, 4.00, 10],
        'Coleslaw': [0, 4.00, 10]
    },
    'Desserts': {
        'Ice Cream': [0, 5.00, 10],
        'Cake': [0, 5.00, 10],
        'Pie': [0, 5.00, 10],
        'Cookies': [0, 5.00, 10],
        'Cheese': [0, 5.00, 10],
        'Boozy Milkshake': [0, 5.00, 10],
        'Sundae': [0, 5.00, 10],
        'Gummi Bears': [0, 5.00, 10],
        'Oranges': [0, 5.00, 10],
        'Jello': [0, 5.00, 10],
        'Boba': [0, 5.00, 10],
        'Brownie': [0, 5.00, 10]
    },
    'Drinks': {
        'Coffee': [0, 3.00, 10],
        'Tea': [0, 3.00, 10],
        'Beer': [0, 5.50, 10],
        'Jack Daniels': [0, 5.50, 10],
        'Cider': [0, 5.50, 10],
        'Bubbles': [0, 5.50, 10],
        'Soda': [0, 3.00, 10],
        'Juice': [0, 3.00, 10],
        'Evian': [0, 1.00, 10],
        'Wine': [0, 5.50, 10],
        'Hunch Punch': [0, 5.50, 10],
        'Seltzer': [0, 1.00, 10]
    }
}


togo_menu = {}


def print_menu():
    """
    prints the restaurant menu
    """
    menu_string = 'Menu:'
    for key, value in menu.items():
        menu_string += '\n{}\n\n'.format(key)
        for k, v in value.items():
            menu_string += k + '${:.2f}\n'.format(v[1]).rjust(25-len(k))
        menu_string += '\n'
    print(menu_string)
    return menu_string


def optional_menu():
    """
    allow user to use their own menu
    """
    global menu
    global togo_menu
    filename = input('Enter your menu file: ').strip()
    try:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            unpacked = []
            category = []
            for row in reader:
                category = [row['Category']]
                unpacked += [[row['Item'], row['Category'], row['Price'], row['Quantity']]]
                togo_menu[category[0]] = {}
        for i in range(len(unpacked)):
            togo_menu[unpacked[i][1]].update({unpacked[i][0]: [0, float(unpacked[i][2]), int(unpacked[i][3])]})
    except (KeyError, FileNotFoundError, IOError):
        print('Not a valid menu file; using default menu.')

    menu = togo_menu
    new_order.input_item()


class Order:
    """
    new class
    """
    def __init__(self):
        self.order_id = uuid4()
        self.subtotal = 0

    def __str__(self):
        return self.display_order()

    def __len__(self):
        counter = 0
        for key, value in menu.items():
            for k, v in value.items():
                if v[0] != 0:
                    counter += v[0]
        return counter

    def __repr__(self):
        print('<Order #{} | Items: {} | Total: ${:.2f}>'.format(self.order_id, self.__len__, self.subtotal * 1.101))

    def print_category(self, order_line):
        """
        prints category
        """
        category_string = '\n{}\n'.format(order_line)
        for key, value in menu[order_line].items():
            category_string += key + '${:.2f}\n'.format(value[1]).rjust(25-len(key))
        print(category_string)
        return category_string

    def add_to_order(self, order_line):
        """
        adds items to user order
        """
        for key, value in menu.items():
            if order_line in value:
                while True:
                    try:
                        order_quantity = int(input('How many orders of ' + order_line + ' would you like?\n> '))
                        if order_quantity > 0:
                            self.add_item(order_line, order_quantity)
                        else:
                            print('Please enter a number between 1-' + str(value[order_line][2]))
                        break
                    except ValueError:
                        print('Please enter a number between 1-' + str(value[order_line][2]))
                break
        else:
            print('Please enter a valid menu item')
            return 'Please enter a valid menu item'

    def add_item(self, order_line, order_quantity):
        """
        adds items to user order
        """
        for key, value in menu.items():
            if order_line in value:
                if order_quantity != 0:
                    if value[order_line][2] < order_quantity:
                        print('Oh no!! We only have ' + str(value[order_line][2]) + ' left. Please order again')
                        self.add_to_order(order_line)
                        return
                    else:
                        value[order_line][0] += order_quantity
                        self.subtotal += value[order_line][1] * order_quantity
                        value[order_line][2] -= order_quantity
                else:
                    value[order_line][0] += order_quantity
                    self.subtotal += value[order_line][1] * order_quantity
                    value[order_line][2] -= order_quantity
        print('{} x{} has been added. Your total is ${:.2f}\n'.format(order_line, order_quantity, self.subtotal * 1.101))

    def remove_prompt(self, order_line):
        """
        prompts self.remove from current order
        """
        order_line = order_line.replace('Remove ', '')
        for key, value in menu.items():
            if order_line in value:
                if value[order_line][0] != 0:
                    while True:
                        try:
                            remove_quantity = int(input('You currently have {}x {} in your cart. Remove how many?\n>'.format(value[order_line][0], order_line)))
                            if remove_quantity > value[order_line][0]:
                                int(input('You only have {}x {} in your cart. Remove how many?\n>'.format(value[order_line][0], order_line)))
                            else:
                                self.remove_item(order_line, remove_quantity)
                            break
                        except ValueError:
                            print('Please enter a number between 1-' + str(value[order_line][0]))
                else:
                    print(order_line + ' is not in your order.')
                    self.input_item()

    def remove_item(self, order_line, remove_quantity):
        """
        removes item from current order
        """
        for key, value in menu.items():
            if order_line in value:
                value[order_line][0] -= remove_quantity
                self.subtotal -= value[order_line][1] * remove_quantity
                value[order_line][2] += remove_quantity
                print('{} x{} has been removed. Your total is ${:.2f}\n'.format(order_line, remove_quantity, self.subtotal * 1.101))
                self.input_item()

    def display_order(self):
        """
        provides display of user order
        """

        order_string = '''\n***********************************************
The Snakes Cafe
"Gettin' Slithered Since 1999"
Seattle, WA

Order #{}
===============================================\n'''.format(self.order_id)

        for key, value in menu.items():
            for k, v in value.items():
                if v[0] != 0:
                    item = '{} x{}'.format(k, v[0])
                    order_string += item + '${:.2f}\n'.format(v[0] * v[1]).rjust(46-len(item))

        order_string += '\n-----------------------------------------------\n'
        order_string += 'Subtotal' + '${:.2f}\n'.format(self.subtotal).rjust(46 - 8)
        order_string += 'Sales Tax' + '${:.2f}\n'.format(self.subtotal * 0.101).rjust(46 - 9)
        order_string += '-----------------------------------------------\n'
        order_string += 'Total Due' + '${:.2f}\n'.format(self.subtotal * 1.101).rjust(46 - 9)

        order_string += '***********************************************\n'

        print(order_string)
        return order_string

    def print_receipt(self):
        """
        creates file of and prints user order
        """
        with open('order-{}.txt'.format(self.order_id), 'w') as f:
            f.write(self.display_order())

    def input_item(self):
        """
        changes order according to user input
        """
        global menu
        order_line = input('What would you like?\n> ').title()
        while order_line != 'Quit':
            if order_line == 'Order':
                self.display_order()
            elif 'Remove' in order_line:
                self.remove_prompt(order_line)
            elif order_line == 'Menu':
                if menu == full_menu:
                    print_menu()
                else:
                    menu = togo_menu
                    print_menu()
            elif order_line == 'Togo':
                optional_menu()
            elif order_line == 'Checkout':
                self.print_receipt()
            elif order_line in menu:
                self.print_category(order_line)
            else:
                self.add_to_order(order_line)
            order_line = input('What would you like?\n> ').title()
        print('Thank you for coming by. See you soon!')
        quit()


if __name__ == '__main__':
    print(intro)
    menu = full_menu
    print_menu()
    print(order_prompt)
    try:
        new_order = Order()
        new_order.input_item()
    except KeyboardInterrupt:
        print('\nThanks for visiting the Snake Cafe.')
