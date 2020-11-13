'''
Created on Nov 12, 2020

@author: Chris Luhring
'''

class Calculator(object):

    def positive(self, dog_or_food) :
        if dog_or_food < 0 :
            raise TypeError(dog_or_food + " must be positive")
            
    def ensure_int(self, dog) :  
        if not isinstance(dog, (int)) :
            raise TypeError(dog + " is a value for the number of dogs")
    
    def ensure_number(self, food) :  
        if not isinstance(food, (int, float)):
            raise TypeError(food + " must be a number or float")
    
    def input_checks(self, small_dogs, medium_dogs, large_dogs, food_supply) :
        # checks small dog input for positive integer
        self.ensure_int(small_dogs)
        self.positive(small_dogs)
        # checks medium dog input for positive integer
        self.ensure_int(medium_dogs)
        self.positive(medium_dogs)
        # checks  dog large dog input for positive integer
        self.ensure_int(large_dogs)
        self.positive(large_dogs)
        # checks dog food input for positive integer or float
        self.ensure_number(food_supply)
        self.positive(food_supply)
    
    
    def dogfood_calc(self, small_dogs, medium_dogs, large_dogs, food_supply) :
        # ensure_number & ensure_positive checks added to check params
        self.input_checks(small_dogs, medium_dogs, large_dogs, food_supply)
        # check to ensure dogs are not more than 30
        if small_dogs + medium_dogs + large_dogs > 30 :
            return("Sorry, you have too many dogs at your shelter")
            
        # calculate food supply need, return 0 if less than 0, add 20%
        else : 
            small_dog_food_needed = small_dogs * 10
            medium_dog_food_needed = medium_dogs * 20
            large_dog_food_needed = large_dogs * 30
            food_supply_needed = small_dog_food_needed + medium_dog_food_needed + large_dog_food_needed - food_supply
            if food_supply_needed < 0 :
                return(0)
            else :
                twenty_percent_extra = food_supply_needed * .2
                total_dog_food_needed = food_supply_needed + twenty_percent_extra
                return(total_dog_food_needed)