from src.parse import get_input
from src.receipt import compute_total, print_receipt


if __name__ == "__main__":

    # exemption set (the tax of 10% is not applied to products containing
    # the words below)
    exemptions = {"chocolate", "chocolates", "bread",
                  "pills", "pill", "drug", "drugs", "medicine", "medicines",
                  "book", "books"}

    item_list = get_input(exemptions)

    total_tax, total_price = compute_total(item_list)

    print_receipt(total_tax, total_price, item_list)
