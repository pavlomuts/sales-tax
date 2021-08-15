
def compute_total(items_list):
    """Computes total taxes and total price for all item s in the list

    :param items_list: List of items
    :type list
    :return: tuple(Tax, Price) or tuple(None, None) if list of items is empty
    :rtype: tuple
    """

    if len(items_list) == 0:
        return None, None

    total_tax = 0
    total_price = 0

    for item in items_list:
        total_tax += item.tax * item.quantity
        total_price += item.price_incl_tax * item.quantity

    # here the result is rounded in order to avoid numbers like 0.15000000000001
    # it returns just 0.15 in this case
    return round(total_tax, 2), round(total_price, 2)


def print_receipt(total_tax, total_price, items_list):
    """Print list of items and their prince including taxes

    :param total_tax: Total taxes to pay
    :type total_tax: float
    :param total_price: Total price to pay
    :type total_price: float
    :param items_list: List of items
    :type items_list: list
    """

    if len(items_list) == 0:
        print("\nThe basket is empty.")
    else:

        print("\n---------Receipt--------")

        for item in items_list:
            print(item)

        print("Sales tax: {:.2f}".format(total_tax))
        print("Total: {:.2f}".format(total_price))
