def remove_prompt(order_line):
        """
        prompts Order.remove from current order
        """
        global subtotal
        order_line = order_line.replace('Remove ', '')
        for key, value in menu.items():
            if order_line in value.keys():
                while True:
                try:
                    remove_quantity = int(input('You currently have {} {} in your cart. Remove how many?\n>'.format(value[order_line][0], order_line)))
                    if remove_quantity > 0:
                        Order.remove_item(order_line, remove_quantity)
                    else:
                        print('You currently have {} {} in your cart. Remove how many?\n>'.format(value[order_line][0], order_line))
                    break
                except ValueError:
                    print('Please enter a number between 1-' + str(value[order_line][2]))




def remove_item(order_line, remove_quantity):
        """
        removes item from current order
        """
        global subtotal
        for key, value in menu.items():
            if order_line in value.keys():
                if remove_quantity != 0:
                    if value[order_line][0] > 0:
                        value[order_line][0] -= remove_quantity
                        subtotal -= value[order_line][1]] * remove_quantity
                        value[order_line][2] += remove_quantity
                        print('{} x{} has been removed. Your total is ${:.2f}\n'.format(order_line, remove_quantity, subtotal * 1.101)
                        break
                    else:

        else:
            print(order_line + ' is not in your order.')
            input_item()
