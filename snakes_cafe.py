
menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************


***********************************
** What would you like to order? **
***********************************"""

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
        'Milk': [0, 3.00],
        'Soda': [0, 3.00],
        'Juice': [0, 3.00],
        'Water': [0, 3.00]
    }
}

order = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Blood of the Innocent': 0
}

print(menu)

order_line = input('> ')

while order_line != 'quit':
    if order_line in order:
        order[order_line] += 1
        print('You have added {} {} to your order'.format(order[order_line], order_line))
        order_line = input('> ')
    else:
        print('Please enter a valid menu item')
        order_line = input('> ')

if __name__ == '__main__':
