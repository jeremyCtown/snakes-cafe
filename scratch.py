def remove_item(order_line):
        """
        prompts Order.remove from current order
        """
        global subtotal
        order_line = order_line.replace('Remove ', '')
        for key, value in menu.items():
            if order_line in value.keys():
                while True:
                try:
                    remove_quantity = int(input('How many orders of ' + order_line + ' would you like?\n> '))
                    if remove_quantity > 0:
                        Order.remove_item(order_line, remove_quantity)
                    else:
                        print('Please enter a number between 1-' + str(value[order_line][0]))
                    break
                except ValueError:
                    print('Please enter a number between 1-' + str(value[order_line][2]))




def remove_item(order_line):
        """
        removes item from current order
        """
        global subtotal
        for key, value in menu.items():
            if order_line in value.keys():
                if order_quantity != 0:
                if value[order_line][0] > 0:
                    value[order_line][0] -= 1
                    value[order_line][2] += 1
                    subtotal -= value[order_line][1]
                    print(order_line + ' has been removed. Your total is ${:.2f}'.format(subtotal * 1.101))
                    break
        else:
            print(order_line + ' is not in your order.')
            input_item()
