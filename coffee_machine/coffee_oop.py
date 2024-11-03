class Coffee():

    def __init__(self , resources: dict , drink: dict) -> bool:

        self.resources = resources
        self.drink = drink

    def check_resources(self): # check how much resources left so we can server next coffee

        for item in self.drink['ingredients']:
          if self.resources[item] < self.drink['ingredients'][item]:
              return f"we do not have enough {item}"
        else:
            return True
        
    def resources_left(self):  # after serving dring deduct resources from all resource

        for item in self.drink['ingredients']:
            self.resources[item] -= self.drink['ingredients'][item]
    
    def calculate_coin_value(self , cost_of_coffee:float, coin_added_by_customer:float): # check if customer have enough money

        self.cost_of_coffee = cost_of_coffee
        self.coin_added_by_customer = coin_added_by_customer

        if self.cost_of_coffee > self.coin_added_by_customer: 
            return f"you don't have enough money here is your money {self.coin_added_by_customer}"
        
        elif self.coin_added_by_customer > self.cost_of_coffee:
            return True
        
        else:
            return False
        


