import math


class Item:
    """Class which stores information about specific item

    :param quantity: Quantity of items
    :type quantity: int
    :param name: Name of the item
    :type name: str
    :param imported: Indicates whether item is imported; if yes, then 5% tax
    is applied
    :type imported: bool
    :param exempt: Indicates whether item is exempt of tax; if not, then 10% is
    applied
    :type exempt: bool
    :param price: Item price
    :type price: float
    :param tax: Item tax
    :type tax: float
    :param price_incl_tax: Item price including all taxes
    :type price_incl_tax: float
    """

    def __init__(self, quantity, name, imported, exempt, price):
        """Constructor method

        :param quantity: Quantity of items
        :type quantity: int
        :param name: Name of the item
        :type name: str
        :param imported: Indicates whether item is imported; if yes, then 5% tax
        is applied
        :type imported: bool
        :param exempt: Indicates whether item is exempt of tax; if not, then 10% is
        applied
        :type exempt: bool
        :param price: Item price
        :type price: float
        """

        self.quantity = quantity
        self.name = name
        self.imported = imported
        self.exempt = exempt
        self.price = price

        self.tax = self.get_tax()
        self.price_incl_tax = self.price + self.tax

    def __str__(self):
        """Method for correct string representation of item"""

        return "{:} {:}: {:.2f}".format(self.quantity, self.name,
                                        self.quantity * self.price_incl_tax)

    def get_tax(self):
        """Method for computing of all taxes for the item

        :return: All taxes
        :rtype: float
        """

        tax = 0

        # if item is not exempt of taxes, then 10% tax is applied
        if not self.exempt:
            tax += self.price * 0.1

        # if item is imported, then 5% taxes is applied
        if self.imported:
            tax += self.price * 0.05

        # rounding up to the nearest 0.05
        tax = math.ceil(tax / 0.05) * 0.05

        # here rounded again in order to avoid numbers like 0.150000000000001
        # it returns just 0.15 in this case
        return round(tax, 2)
