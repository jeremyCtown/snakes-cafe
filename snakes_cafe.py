"""
command line menu program
"""
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
        'Vegatarian Option': [0, 10.00]
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

def print_menu():
    """
    prints the restaurant menu
    """
    print('Menu:\n')
    for key, value in menu.items():
        print(key)
        for k, v in value.items():
            print(k, v[1])
        print()


def input_item():
    """
    user inputs item to order
    """
    global subtotal
    order_line = input('> ').title()
    while order_line != 'Quit':
    # if order_line == 'Quit':
    #     print('Bye!')
    #     quit()
        if order_line == 'Order':
            print('yes')
            # TODO  print order
        elif order_line == 'Remove'
        else:
            for key, value in menu.items():
                if order_line in value.keys():
                    value[order_line][0] += 1
                    subtotal += value[order_line][1]
                    print(subtotal)
                else:
                    print('Please enter a valid menu item')
        order_line = input('> ').title()
    print('Thank you for your order!')
    quit()
    # return subtotal

# def order_total_cost():

    # while order_line != 'quit':
    #     if order_line in menu[key][key]:
    #         print('ordered')
    #         # order[order_line] += 1
    #         # print('You have added {} {} to your order'.format(order[order_line], order_line))
    #         print(order_prompt)
    #     else:
    #         print('Please enter a valid menu item')
    #         print(order_prompt)

    # return order_line


if __name__ == '__main__':
    print(intro)
    print_menu()
    print(order_prompt)
    # subtotal = input_item(subtotal)
    input_item()
