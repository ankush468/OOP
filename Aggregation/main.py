class Customer:

    def __init__(self, name, gender, address):

        self.name=name
        self.gender = gender
        self.address = address

class Address:

    def __init__(self, city, pincode, state):

        self.city=city
        self.pincode = pincode
        self.state = state


add= Address('kolkata', 122001, 'wb' )
cust = Customer('nitish', 'male', add)

print(cust)
