class Customer:

    def __init__(self, name, gender, address):

        self.name=name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):

        self.name = new_name
        self.address.chnage_address(new_city,new_pin,new_state)

class Address:

    def __init__(self, city, pincode, state):

        self.city=city
        self.pincode = pincode
        self.state = state
    
    def chnage_address(self, new_city, new_pin, new_state):

        self.city = new_city
        self.pincode = new_pin
        self.state = new_state

add= Address('kolkata', 700156, 'wb' )
cust = Customer('nitish', 'male', add)

print(cust.address.city)

cust.edit_profile("ankush","Gurgaon", 122001, "haryana")
print(cust.address.city)

# logic
# we have initilize bot class (add=Address) and (cust=Customer) so self for class Addess=add and self for Customer=cust
# within cust we have initilize class object add which have add the Address class attribute.
# now we print cust which is self for class Customer cust.address(conatin whole Address class) so we need to print cust.address.city
# now we chnaged values for cust with edit profile method we passed parameter 
# now edit profile is calling chnage_address method we can call this method becuase cust is initilizing add which is instence of Address done
