"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about user."""

        return (
            f"<Customer: {self.first_name} {self.last_name}, {self.password}>"
        )


def read_customers_from_file(filepath):
    """Read customers from file and populate dictionary of customers.

    Dictionary will be {email: Customer object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            first_name, last_name, email, password = line.strip().split("|")
            customers[email] = Customer(first_name, last_name, email, password)

    return customers


def get_by_email(email):
    """Given an email address, return matching Customer."""

    # This relies on access to the global dictionary `customers`

    return customers[email]


# Dictionary to hold customers

customers = read_customers_from_file("customers.txt")
