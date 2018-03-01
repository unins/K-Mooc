#! python
import os
import sys
import datetime
""" file-docs : OPEN A RESTAURANT : Making Order System
  (1) to Show MENU_PAN = MENU_PAN (changeable)
  (2) to Input order = by Item index & quantity
  (3) to Calculate the Bills = Including (Tax= 6.5%, Tip= 10%)

 * Release Note : correct sorting version
    - Dict can not be ordered / arrange 'list' first.
    - Question : _arr.sort() = None. sorted(_arr) = 'list' O.K
    - I don't know the differences btw .sort() & sorted()
"""
SEPARATOR = '__'*22
MENU_DICT = {
    1 : ['GRILLED_LAMB_CHOPS', 34900],
    2 : ['PAN-FRIED_SCALLOPS', 26500],
    3 : ['SCRAMBLED_EGGS_AND_SMOKED_SALMON', 33500],
    4 : ['BEEF_WELLINGTON', 43500],
    5 : ['STUFFED_ROAST_CHICKEN', 23000],
    6 : ['CHRISTMAS_BOMBE', 37000],
    7 : ['STUFFED_RIB_OF_BEEF', 28000],
    8 : ['YORKSHIRE_PUDDING ', 16500],
    9 : ['ROAST_CHICKEN', 21000],
    10 : ['STUFFED_PORK_TENDERLOIN', 32700],
    11 : ['HORSERADISH_YORKSHIRE_PUDDING', 13800],
    12 : ['ROAST_BEEF_CARPACCIO', 35500],
    13 : ['STUFFED_LAMB_WITH_SPINACH_AND_PINE_NUTS', 42200],
    14 : ['ROAST_BEEF_WITH_CARAMELISED_ONION_GRAVY', 45800],
    15 : ['MACARONI_CHEESE_AND_CAULIFLOWER_BAKE', 19800],
    16 : ['BEEF_EMPANADA', 22500],
    17 : ['MOZZARELLA_&_ROSEMARY_PIZZA', 21000],
    18 : ['APRICOT_AND_FRANGIPANE_TART', 5800],
    19 : ['PINEAPPLE_DESSERT_WITH_CARAMEL', 7500],
    20 : ['FISH_&_CHIPS', 9500],
    21 : ['ESPRESSO_PANNA_COTTA', 7500],
    }
MENU_PAN_FORMAT = ""                                        +\
    "-------------------------------------------------\n  " +\
    "    MENU-PAN  / Gordon-Ramsay's Restautant       \n"   +\
    "-------------------------------------------------\n"   +\
    "%s"                                                    +\
    "-------------------------------------------------\n"
BILL_FORMAT = ""                                            +\
    "-------------------------------------------------\n"   +\
    "    $$$ BILL / Gordon-Ramsay's Restautant $$$    \n"   +\
    "-------------------------------------------------\n"   +\
    "%s"                                                    +\
    "-------------------------------------------------\n"

# for n in range(len(MENU_DICT)):
#     print('%s. %s' %(n+1, MENU_DICT[n+1][0]), ' ' * (15 - len(MENU_DICT[n+1][0])), '.' * 8, '%s won' %MENU_DICT[n+1][1])
RATE_TAX = float(6.5/100)
RATE_TIP = float(11/100)

def show_menu_pan():
    menu_string = ''
    for i, item_arr in enumerate(MENU_DICT.values(), 1):
        # print('%s. %-16s ........ %4s won' %(i, item_arr[0], item_arr[1]))
        menu_string += (' {:2}. {:40} {:.<8} {:>6,} won\n'.format(
        i, item_arr[0],
        '.',
        item_arr[1]))
    print(MENU_PAN_FORMAT %menu_string)

def get_input_str():
    input_message = 'Please, order menu by index-quantity & space\n'
    return input(input_message)

def get_order_dict_from(input_str):
    menu_arr = input_str.strip().split()

    order_dict = {}
    for menu in menu_arr:
        _key = int(menu.split('-')[0])
        _value = int(menu.split('-')[1])
        order_dict[_key] = _value
    return order_dict

show_menu_pan()
input_str = get_input_str()
order_dict = get_order_dict_from(input_str)

def get_order_bill_calculation(order_dict, RATE_TAX, RATE_TIP):
    order_bill_str = ''
    menu_total = 0
    tax = 0
    for index, _key in enumerate(order_dict.keys(), 1):
        menu_name = MENU_DICT[_key][0]
        menu_price = MENU_DICT[_key][1]
        menu_quantity = order_dict[_key]
        order_bill_str += (' {}. {:16} {:>6,} x {:2} = {:>7,} won\n'.format(
            index,
            menu_name,
            menu_price,
            menu_quantity,
            menu_price * menu_quantity
        ))
        tax += menu_price * RATE_TAX
        menu_total += menu_price * menu_quantity
    return order_bill_str, menu_total, tax

tip = 0
menu_total_tax_n_tip = 0
order_bill_str, menu_total, tax = get_order_bill_calculation(order_dict, RATE_TAX, RATE_TIP)

tip = menu_total * RATE_TIP
menu_total_tax_n_tip += menu_total + tax + tip
menu_total_tax_n_tip_fix = int(menu_total_tax_n_tip/100) * 100

print(BILL_FORMAT %order_bill_str)
print(('     MENU PRICE {:.<16} {:>7,} won').format('.',int(menu_total)))
print(('            TAX {:.<16} {:>7,} won').format('.',int(tax)))
print(('            TIP {:.<16} {:>7,} won').format('.',int(tip)))
print(('    TOTAL PRICE {:.<16} {:>7,} won').format('.',int(menu_total_tax_n_tip)))
print(('  PAYMENT PRICE {:.<16} {:>7,} won').format('.',int(menu_total_tax_n_tip_fix)))
