import snakes_cafe as sc


def test_print_menu():
    """
    test the print menu function
    """
    sc.menu = sc.full_menu
    assert sc.print_menu() == '''Menu:
Appetizers

Wings              $2.00
Calamari           $2.00
Spring Rolls       $2.00
Nachos             $2.00
Spinach Dip        $2.00
Sampler            $2.00
Mozz Sticks        $2.00
Corn Doggies       $2.00
Hummus             $2.00
Almonds            $2.00
Chips              $2.00
Oreos              $2.00


Entrees

Salmon            $10.00
Steak             $10.00
Tacos             $10.00
Salad             $10.00
Pizza             $10.00
Vegetarian Delight$10.00
Pasta             $10.00
Ribs              $10.00
Burrito           $10.00
Grilled Chicken   $10.00
Fried Fish        $10.00
S'ghetti          $10.00


Sides

French Fries       $4.00
Hush Puppies       $4.00
Green Beans        $4.00
Mashed Potatoes    $4.00
Corn               $4.00
Rolls              $4.00
Carrots            $4.00
Biscuits           $4.00
Mac and Cheese     $4.00
Spinach            $4.00
Asparagus          $4.00
Coleslaw           $4.00


Desserts

Ice Cream          $5.00
Cake               $5.00
Pie                $5.00
Cookies            $5.00
Cheese             $5.00
Boozy Milkshake    $5.00
Sundae             $5.00
Gummi Bears        $5.00
Oranges            $5.00
Jello              $5.00
Boba               $5.00
Brownie            $5.00


Drinks

Coffee             $3.00
Tea                $3.00
Beer               $5.50
Jack Daniels       $5.50
Cider              $5.50
Bubbles            $5.50
Soda               $3.00
Juice              $3.00
Evian              $1.00
Wine               $5.50
Hunch Punch        $5.50
Seltzer            $1.00\n\n'''


def test_print_category():
    """
    test that a category is printed
    """
    sc.menu = sc.full_menu
    sc.new_order = sc.Order()
    assert sc.new_order.print_category('Appetizers') == '''\nAppetizers
Wings              $2.00
Calamari           $2.00
Spring Rolls       $2.00
Nachos             $2.00
Spinach Dip        $2.00
Sampler            $2.00
Mozz Sticks        $2.00
Corn Doggies       $2.00
Hummus             $2.00
Almonds            $2.00
Chips              $2.00
Oreos              $2.00\n'''


def test_display_order():
    """
    test if current order prints
    """
    sc.menu = sc.full_menu
    sc.new_order = sc.Order()
    assert 'Total Due' in sc.new_order.display_order()


def test_remove_invalid_item():
    """
    test that you are removing an item
    """
    sc.menu = sc.full_menu
    sc.new_order = sc.Order()
    assert sc.new_order.remove_prompt('Cheese') == 'Cheese is not in your order.'


def test_add_invalid_item_to_order():
    """
    test that an item gets added to order
    """
    sc.menu = sc.full_menu
    sc.new_order = sc.Order()
    assert sc.new_order.add_to_order('wangs') == 'Please enter a valid menu item'


def test__len__():
    """test that an UUID is made"""
    sc.menu = sc.full_menu
    sc.new_order = sc.Order()
    sc.new_order.add_item('Wine', 1)
    assert len(sc.new_order) == 1


def test__str__():
    """test that an UUID is made"""
    sc.menu = sc.full_menu
    sc.new_order = sc.Order()
    sc.new_order.add_item('Wine', 1)
    assert 'Total Due' in str(sc.new_order)


def test_print_receipt():
    """test to print a receipt"""
    sc.menu = sc.full_menu
    sc.new_order = sc.Order()
