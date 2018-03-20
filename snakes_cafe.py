
menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Blood of the Innocent

***********************************
** What would you like to order? **
***********************************"""

print(menu)

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

order_line = input('> ')
print(order_line)

if order_line in order:
    order[order_line] += 1
    print('You have added {} {} to your order'.format(order[order_line], order_line))
    print('Test')
else:
    print('Please enter a valid menu item')
    order_line
