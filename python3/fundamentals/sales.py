tax_percentage = 0.1
discount_percentage = 0.05


def calculate_discount(amount):
    return amount * discount_percentage


def calculate_tax(amount):
    return amount * tax_percentage


def calculate_total_amount(amount):
    return amount + calculate_tax(amount) - calculate_discount(amount)


if __name__ == "__main__":
    print("Sales started")
    print("Default discount percentage:", tax_percentage)
    print("Default tax percentage:", tax_percentage)
