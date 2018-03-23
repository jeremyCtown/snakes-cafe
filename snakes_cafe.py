"""
command line menu program
"""

from uuid import uuid4
import csv

order_id = uuid4()

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

menu = {
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

order_line = ''
subtotal = 0


def print_menu():
    """
    prints the restaurant menu
    """
    menu_string = 'Menu:'
    for key, value in menu.items():
        menu_string += '\n' + key + '\n\n'
        for k, v in value.items():
            menu_string += k + '${:.2f}\n'.format(v[1]).rjust(25-len(k))
        menu_string += '\n'
    print(menu_string)
    return menu_string


def print_category(order_line):
    """
    prints category
    """
    category_string = '\n' + order_line + '\n'
    for key, value in menu[order_line].items():
        category_string += key + '${:.2f}'.format(value[1]).rjust(25-len(key)) + '\n'
    print(category_string)
    return category_string


def add_to_order(order_line):
    """
    adds items to user order
    """
    global subtotal
    for key, value in menu.items():
        if order_line in value.keys():
            while True:
                try:
                    order_quantity = int(input('How many orders of ' + order_line + ' would you like?\n> '))
                    if order_quantity > 0:
                        Order.add_item(order_line, order_quantity)
                    else:
                        print('Please enter a number between 1-' + str(value[order_line][2]))
                    break
                except ValueError:
                    print('Please enter a number between 1-' + str(value[order_line][2]))
            break
    else:
        print('Please enter a valid menu item')
        return 'Please enter a valid menu item'


def input_item():
    """
    changes order according to user input
    """
    global subtotal
    order_line = input('What would you like?\n> ').title()
    while order_line != 'Quit':
        if order_line == 'Order':
            Order.display_order()
        elif 'Remove' in order_line:
            Order.remove_item(order_line)
        elif order_line == 'Menu':
            print_menu()
        elif order_line == 'Checkout':
            Order.print_receipt()
        elif order_line == 'Togo':
            optional_menu()
        elif order_line in menu:
            print_category(order_line)
        else:
            add_to_order(order_line)
        order_line = input('What would you like?\n> ').title()
    print('Thank you for your order!')
    quit()


def optional_menu():
    """
    allow user to use their own menu
    """
    filename = input('Enter your menu file: ').strip()

    try:
        # edit code block below to verify menu file is csv and can be used
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            unpacked = []
            category = []
            menu = {}
            for row in reader:
                category = [row['Category']]
                unpacked += [[row['Item'], row['Category'], row['Price'], row['Quantity']]]
                menu[category[0]] = ''

            # for row in reader:
            #     menu[unpacked[1]] = {unpacked[0]: [0, unpacked[2], unpacked[3]]}

            # print(menu)
            # print(unpacked)
            make_menu(menu, unpacked)

                # print(row['Item'], row['Category'], row['Price'], row['Quantity'])
                # print(unpacked)
                # menu.update({unpacked[0]: [0, unpacked[2], unpacked[3]]})
                # if menu[unpacked[1]] not in menu:
                #     print('test')
                #     # menu[unpacked[1]] = {unpacked[0]: [0, unpacked[2], unpacked[3]]}
                # print(menu)
                # else:

            # print(unpacked)

    except:
        print('Not a valid menu file; using default menu.')

    input_item()


# def make_menu(menu, unpacked):
#     for i in unpacked:
#         if unpacked[i][1] in menu:
#             menu[unpacked[i][1]] = {unpacked[i][0]: [0, unpacked[i][1], unpacked[i][2]]}
#     print(menu)


class Order:
    """
    new class
    """
    def __init__(self):
        self.default

    def __str__(self):
        return 'Welcome to Snakes Cafe'

    def __len__(self):
        counter = 0
        for key, value in menu.items():
            for k, v in value.items():
                if v[0] != 0:
                    counter += v[0]
        return counter

    def __repr__(self):
        print('<Order #{} | Items: {} | Total: ${:.2f}>'.format(order_id, Order.__len__, subtotal * 1.101))

    def add_item(order_line, order_quantity):
        """
        adds items to user order
        """
        global subtotal
        for key, value in menu.items():
            if order_line in value.keys():
                if order_quantity != 0:
                    if value[order_line][2] < order_quantity:
                        print('Oh no!! We only have ' + str(value[order_line][2]) + ' left. Please order again')
                        add_to_order(order_line)
                        return
                    else:
                        value[order_line][0] += order_quantity
                        subtotal += value[order_line][1] * order_quantity
                        value[order_line][2] -= order_quantity
                else:
                    value[order_line][0] += order_quantity
                    subtotal += value[order_line][1] * order_quantity
                    value[order_line][2] -= order_quantity
        print('{} x{} has been added. Your total is ${:.2f}\n'.format(order_line, order_quantity, subtotal * 1.101))

    def remove_item(order_line):
        """
        removes item from current order
        """
        global subtotal
        order_line = order_line.replace('Remove ', '')
        for key, value in menu.items():
            if order_line in value.keys():
                if value[order_line][0] > 0:
                    value[order_line][0] -= 1
                    value[order_line][2] += 1
                    subtotal -= value[order_line][1]
                    print(order_line + ' has been removed. Your total is ${:.2f}'.format(subtotal * 1.101))
                    break
        else:
            print(order_line + ' is not in your order. Please remove a valid item')

    def display_order():
        """
        provides display of user order
        """

        order_string = '''\n***********************************************
The Snakes Cafe
Seattle, WA

Order #{}
===============================================\n'''.format(order_id)

        for key, value in menu.items():
            for k, v in value.items():
                if v[0] != 0:
                    item = '{} x{}'.format(k, v[0])
                    order_string += item + '${:.2f}'.format(v[0] * v[1]).rjust(46-len(item)) + '\n'

        order_string += '\n-----------------------------------------------' + '\n'
        order_string += 'Subtotal' + '${:.2f}'.format(subtotal).rjust(46 - 8) + '\n'
        order_string += 'Sales Tax' + '${:.2f}'.format(subtotal * 0.101).rjust(46 - 9) + '\n'
        order_string += '-----------------------------------------------' + '\n'
        order_string += 'Total Due' + '${:.2f}'.format(subtotal * 1.101).rjust(46 - 9) + '\n'

        order_string += '***********************************************' + '\n'

        print(order_string)
        print(Order.__len__)
        return order_string

    def print_receipt():
        """
        creates file of and prints user order
        """
        with open('order-{}.txt'.format(order_id), 'w') as f:
            f.write(Order.display_order())


if __name__ == '__main__':
    print(intro)
    print_menu()
    print(order_prompt)
    try:
        input_item()
    except KeyboardInterrupt:
        print('\nThanks for visiting the Snake Cafe.')
