import pytest
import snakes_cafe


def test_print_menu():
    '''
    test the print menu function
    '''
    assert snakes_cafe.print_menu() == '''Menu:
Appetizers

Wings               2.00
Calamari            2.00
Spring Rolls        2.00
Nachos              2.00
Spinach Dip         2.00
Sampler             2.00


Entrees

Salmon             10.00
Steak              10.00
Tacos              10.00
Salad              10.00
Pizza              10.00
Vegetarian Option  10.00


Sides

French Fries        4.00
Hush Puppies        4.00
Green Beans         4.00
Mashed Potatoes     4.00
Corn                4.00
Rolls               4.00


Desserts

Ice Cream           5.00
Cake                5.00
Pie                 5.00
Cookies             5.00
Cheese              5.00
Boozy Milkshake     5.00


Drinks

Coffee              3.00
Tea                 3.00
Beer                5.50
Soda                3.00
Juice               3.00
Evian               1.00\n\n'''


def test_print_order():
    '''
    test if current order prints
    '''
    assert snakes_cafe.print_order


def test_remove_item():
    '''
    test that you are removing an item
    '''
    snakes_cafe.add_to_order('Wings')
    snakes_cafe.remove_item('Wings')
    assert snakes_cafe.menu['Appetizers']['Wings'][0] == 0


def test_print_category():
    '''
    test that a category is printed
    '''
    assert snakes_cafe.print_category('Appetizers') == '''\nAppetizers
Wings                2.00
Calamari             2.00
Spring Rolls         2.00
Nachos               2.00
Spinach Dip          2.00
Sampler              2.00\n'''


def test_add_to_order():
    '''
    test that an item gets added to order
    '''
    snakes_cafe.add_to_order('Wings')
    assert snakes_cafe.menu['Appetizers']['Wings'][0] == 1
    assert snakes_cafe.add_to_order('wangs') == 'Please enter a valid menu item'


# def test_input_item - not needed at this time, relies on user input
