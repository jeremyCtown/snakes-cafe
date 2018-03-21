"""
command line menu program
"""

import uuid

intro = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
'''

order_prompt = '''
**********************************************************************
** What would you like to order?                                    **
** To add an item to your order, type the item name                 **
** To remove an item from your order, type the "remove <item name>" **
** To see your current order, type "order"                          **
** To quit at any time, type "quit"                                 **
**********************************************************************
\n'''

menu = {
    'Appetizers': {
        'Wings': [0, 2.00],
        'Calamari': [0, 2.00],
        'Spring Rolls': [0, 2.00],
        'Nachos': [0, 2.00],
        'Spinach Dip': [0, 2.00],
        'Sampler': [0, 2.00]
    },
    'Entrees': {
        'Salmon': [0, 10.00],
        'Steak': [0, 10.00],
        'Tacos': [0, 10.00],
        'Salad': [0, 10.00],
        'Pizza': [0, 10.00],
        'Vegetarian Option': [0, 10.00]
    },
    'Sides': {
        'French Fries': [0, 4.00],
        'Hush Puppies': [0, 4.00],
        'Green Beans': [0, 4.00],
        'Mashed Potatoes': [0, 4.00],
        'Corn': [0, 4.00],
        'Rolls': [0, 4.00]
    },
    'Desserts': {
        'Ice Cream': [0, 5.00],
        'Cake': [0, 5.00],
        'Pie': [0, 5.00],
        'Cookies': [0, 5.00],
        'Cheese': [0, 5.00],
        'Boozy Milkshake': [0, 5.00]
    },
    'Drinks': {
        'Coffee': [0, 3.00],
        'Tea': [0, 3.00],
        'Beer': [0, 5.50],
        'Soda': [0, 3.00],
        'Juice': [0, 3.00],
        'Evian': [0, 1.00]
    }
}

order_line = ''
subtotal = 0
# taxes = str(subtotal * 0.101)
# total = str(subtotal * 1.101)


def print_menu():
    """
    prints the restaurant menu
    """
    menu_string = 'Menu:'
    for key, value in menu.items():
        menu_string += '\n' + key + '\n\n'
        for k, v in value.items():
            menu_string += k + '{:.2f}\n'.format(v[1]).rjust(25-len(k))
        menu_string += '\n'
    print(menu_string)
    return menu_string


def print_order():
    """
    provides print out of user order
    """
    print(
    '''\n***********************************************
The Snakes Cafe
Seattle, WA

Order #{}
===============================================\n'''.format(uuid.uuid4()))

    for key, value in menu.items():
        for k, v in value.items():
            if v[0] != 0:
                item = '{} x{}'.format(k, v[0])
                print(item, '${:.2f}'.format(v[0] * v[1]).rjust(46-len(item)))
    print()

    print('-----------------------------------------------')

    print('Subtotal', '${:.2f}'.format(subtotal).rjust(46 - 8))

    print('Sales Tax', '${:.2f}'.format(subtotal * 0.101).rjust(46 - 9))
    print('-----------------------------------------------')
    print('Total Due', '${:.2f}'.format(subtotal * 1.101).rjust(46 - 9))

    print(
    '''***********************************************
    '''
    )
    # TODO  print order


def remove_item(order_line):
    """
    removes item from user order
    """
    global subtotal
    order_line = order_line.replace('Remove ', '')
    for key, value in menu.items():
        if order_line in value.keys():
            value[order_line][0] -= 1
            subtotal -= value[order_line][1]
            print(order_line + ' has been removed. Your total is ${:.2f}'.format(subtotal * 1.101))
            break
    else:
        print('Please remove a valid menu item')


def print_category(order_line):
    """
    prints category
    """
    print('\n' + order_line + '\n')
    for key, value in menu[order_line].items():
        print(key, '{:.2f}'.format(value[1]).rjust(25-len(key)))
    print()


def add_to_order(order_line):
    """
    adds items to user order
    """
    print(order_line)
    global subtotal
    for key, value in menu.items():
        if order_line in value.keys():
            value[order_line][0] += 1
            subtotal += value[order_line][1]
            print(order_line + ' has been added. Your total is ${:.2f}'.format(subtotal * 1.101))
            break
    else:
        print('Please enter a valid menu item')
        return 'Please enter a valid menu item'


def input_item():
    """
    changes order according to user input
    """
    global subtotal
    order_line = input('> ').title()
    while order_line != 'Quit':
        if order_line == 'Order':
            print_order()
        elif 'Remove' in order_line:
            remove_item(order_line)
        elif order_line == 'Menu':
            print_menu()
        elif order_line in menu:
            print_category(order_line)
        else:
            add_to_order(order_line)
        order_line = input('> ').title()
    print('Thank you for your order!')
    quit()


if __name__ == '__main__':
    print(intro)
    print_menu()
    print(order_prompt)
    input_item()
