from src.item import Item


def is_float(s):
    """Checks whether given string can be converted to float

    :param s: Given string
    :type s: str
    :return: True - can converted, False - otherwise
    :rtype: bool
    """

    try:
        float(s)
        return True
    except ValueError:
        return False


def check_import(name):
    """Check whether item is imported by its name

    :param name: List of words building the name of item
    :type name: list
    :return: True - the item is imported, False - otherwise
    """

    for word in name:
        if word == "imported":
            return True

    return False


def check_exemption(name, exemptions):
    """Check whether item is exempt of tax. The set of exemptions is given

    :param name: List of words that building item name
    :type name: list
    :param exemptions: Set of exemption
    :type exemptions: set
    :return: True - the item is exempt of taxes, False - otherwise
    :rtype: bool
    """

    for word in name:
        if word in exemptions:
            return True

    return False


def create_item(item_words, exemptions):
    """Creates item by checking whether all information is given correctly and
    identifying whether item is imported and exempt if sales tax

    :param item_words: List of words containing all information about the item
    :type item_words: list
    :param exemptions: Set of predefined exemptions
    :type exemptions: set
    :return: Item object, if the price is given correctly, None otherwise
    :rtype: Item or None
    """

    new_item = None

    # check whether the price is given correctly, if not it will fail
    # to create an item
    if is_float(item_words[-1]) and item_words[-2] == "at":

        name = item_words[1:len(item_words) - 2]

        imported = check_import(name)
        exempt = check_exemption(name, exemptions)

        new_item = Item(int(item_words[0]), " ".join(name),  imported,
                        exempt, float(item_words[-1]))

    return new_item


def get_input(exemptions):
    """Gets the input from terminal and processes it. Saves the results in the
    list of items

    :param exemptions: Set of predefined exemptions
    :type exemptions: set
    :return: List of items
    :rtype: list
    """

    print("Generate receipt for given items.\n"
          "Type the items below, type \"help\" for an input example, "
          "type \"print\" to print the receipt.")

    item_list = []

    while True:

        # get the input from terminal
        line = input()

        # split the line into words using whitespace as delimiter
        words = line.split(" ")

        # check if the first word is a number. Note it will work only if number
        # is as integer, e.g. '1'. Entering '1.0' will fail
        if words[0].isnumeric():

            # process and create the item
            new_item = create_item(words, exemptions)

            if new_item:
                item_list.append(new_item)
                print("Item(s) is(are) added successfully to the basket.")
            else:
                print("Incorrect input of the price, please see the example by "
                      "typing \"help\".")

        # get help
        elif words[0] == "help":

            print("\nExample of correct input:")
            print("1 imported bottle of perfume at 27.99\n")

            print("Each new entry must be followed by a new line.\n")

            print("To print the receipt type \"print\".")

        # stop getting the input and exit the loop to print the receipt
        elif words[0] == "print":
            break
        else:
            print("Unrecognized input, please see the example by typing "
                  "\"help\".")

    return item_list
