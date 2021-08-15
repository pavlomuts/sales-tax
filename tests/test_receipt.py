import unittest

from src.item import Item
from src.parse import is_float, check_import, check_exemption, create_item
from src.receipt import compute_total


class TestReceipt(unittest.TestCase):

    def setUp(self):
        """Create exemption set which will be used in several test cases"""

        # define exemptions
        self.exemptions = {"chocolate", "chocolates", "bread",
                           "pills", "pill", "drug", "drugs", "medicine",
                           "medicines",
                           "book", "books"}

    def test_get_tax(self):
        """Check tax computation with get_tax of Item class"""

        quantity = 1
        name = "beer"
        imported = True
        exempt = True
        price = 1.29
        item = Item(quantity, name, imported, exempt, price)

        self.assertEqual(item.get_tax(), 0.1)

        # change import to False
        item.imported = False
        self.assertEqual(item.get_tax(), 0)

        # change exemption to False
        item.imported = True
        item.exempt = False
        self.assertEqual(item.get_tax(), 0.2)

        # change exemption and import to False
        item.imported = False
        self.assertEqual(item.get_tax(), 0.15)

    def test_is_float(self):
        """Test function is_float, i.e. whether string can be
        converted to float"""

        self.assertEqual(is_float("2.5"), True)
        self.assertEqual(is_float("1"), True)
        self.assertEqual(is_float("b"), False)

    def test_check_import(self):
        """Test function check_import """

        self.assertEqual(check_import(["imported", "chocolate"]), True)
        self.assertEqual(check_import(["chocolate"]), False)

    def test_check_exemption(self):
        """Test function check_exemption"""

        self.assertEqual(check_exemption(["book"], self.exemptions), True)
        self.assertEqual(check_exemption(["bottle", "of", "wine"],
                                         self.exemptions), False)

    def test_parse_item(self):
        """Test creation of Item"""

        item_words = ["1", "book", "at", "15.15"]
        # the instance of Item must be created
        self.assertNotEqual(create_item(item_words, self.exemptions), None)

        # remove "at" from item_words
        item_words = ["1", "book", "15.15"]
        # the instance of Item must not be created
        self.assertEqual(create_item(item_words, self.exemptions), None)

    def test_compute_total(self):
        """Test computation of total tax and total price"""

        # case with no items in basket
        self.assertEqual(compute_total([]), (None, None))

        # add several items to the list knowing in advance that they will be ok
        # to create
        items_list = []

        # item 1
        item = create_item("1 imported bottle of perfume at 27.99".split(" "),
                           self.exemptions)
        items_list.append(item)

        # item 2
        item = create_item("1 bottle of perfume at 18.99".split(" "),
                           self.exemptions)
        items_list.append(item)

        # item 3
        item = create_item("1 packet of headache pills at 9.75".split(" "),
                           self.exemptions)
        items_list.append(item)

        # item 4
        item = create_item("1 box of imported chocolates at 11.25".split(" "),
                           self.exemptions)
        items_list.append(item)

        # test
        self.assertEqual(compute_total(items_list), (6.7, 74.68))


if __name__ == '__main__':
    unittest.main()
