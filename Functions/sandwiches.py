def sandwiches(*items):
    """
    A function that accepts a list of items a person wants on a sandwich.
    :param items: Items needed in sandwich
    :return: print a summary of the sandwich that is being ordered.
    """
    print("\nMaking a Sandwich with the following items:")
    for item in items:
        print("- " + item)


sandwiches('tomato', 'lettuce', 'sardine', 'cucumber')
sandwiches('tomato')
