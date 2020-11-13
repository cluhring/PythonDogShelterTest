'''
Created on Nov 12, 2020

@author: Chris L
'''
import unittest
from dogshelter.calculator import Calculator

class TestDogShelter(unittest.TestCase):    
    
    def testHappy(self):
        calculator = Calculator()
        result = calculator.dogfood_calc(small_dogs=5, medium_dogs=3, large_dogs=7, food_supply=17)
        self.assertEqual(result, 363.6, "FAIL: Happy Path")
    
    def testTrippleHappy(self):
        calculator = Calculator()
        dogs = [10, 9, 8]
        food = [30, 20, 25]
        expected_results = [684.0, 624.0, 546.0]
        for x in range(3):
            result = calculator.dogfood_calc(small_dogs=dogs[x], medium_dogs=dogs[x], large_dogs=dogs[x], food_supply=food[x])
            self.assertEqual(result, expected_results[x], "FAIL: Tripple Happy Path")
    
    # AC: 30 Dog Limit: Expected 31 dogs to return Error message
    def testDogLimit(self):
        calculator = Calculator()
        result = calculator.dogfood_calc(small_dogs=5, medium_dogs=5, large_dogs=21, food_supply=20)
        self.assertEqual(result, "Sorry, you have too many dogs at your shelter", "FAIL: Function doesn't limit dogs")
    
    # Edge case: If no dogs in shelter, 20% of zero is 0
    def testZeroDogs(self):
        calculator = Calculator()
        result = calculator.dogfood_calc(small_dogs=0, medium_dogs=0, large_dogs=0, food_supply=20)
        self.assertEqual(result, 0, "FAIL: Function doesn't limit dogs")
    
    # Edge case: If more food on hand than needed, function should return 0
    def testMorFoodThanNeeded(self):
        calculator = Calculator()
        result = calculator.dogfood_calc(small_dogs=0, medium_dogs=5, large_dogs=0, food_supply=120.1)
        self.assertEqual(result, 0, "FAIL: If shelter has more dog food than needed, return 0")
    
    # Edge case: Expected Error w/ Negative Small Dog
    def testNegativeSmallDog(self):
        calculator = Calculator()
        with self.assertRaises(TypeError) as error:
            calculator.dogfood_calc(small_dogs=-5, medium_dogs=8, large_dogs=4.5, food_supply=20)
        self.assertEqual(str(error.exception), "unsupported operand type(s) for +: 'int' and 'str'")
    
    # Unit test of positive function only
    def testNegativeDogs(self):
        positive_nums = [0, 20.4, 3, 100]
        negative_nums = [-2, -1, -9.3, -200]
        calculator = Calculator()
        for x in range(4) :
            positive_num_exception_raised = False
            negative_num_exception_raised = False
            try:
                calculator.positive(positive_nums[x])
            except:
                positive_num_exception_raised = True
            try:
                calculator.positive(negative_nums[x])
            except:
                negative_num_exception_raised = True
                
            self.assertEqual(False, positive_num_exception_raised, "Exception raised for Positive Number: " + str(positive_nums[x]))
            self.assertEqual(True, negative_num_exception_raised, "No Exception raised for Negative Number: " + str(negative_nums[x]))
    
    # Input Error, Expected Error w/ String Medium Dog
    def testStringMediumDog(self):
        calculator = Calculator()
        with self.assertRaises(TypeError) as error:
            calculator.dogfood_calc(small_dogs=5, medium_dogs="Hello", large_dogs=21, food_supply=20)
        self.assertEqual(str(error.exception), "Hello is a value for the number of dogs")
    
    # Input Error, Expected Error w/ Float Large Dog
    def testLargeDog(self):
        calculator = Calculator()
        with self.assertRaises(TypeError) as error:
            calculator.dogfood_calc(small_dogs=5, medium_dogs=8, large_dogs=4.5, food_supply=20)
        self.assertEqual(str(error.exception), "unsupported operand type(s) for +: 'float' and 'str'")

    # Unit test of integer check function
    def testIntegerFunction(self):
        integers = [0, 20, -3, -100, 10000]
        non_integers = [-2.3, "Yolo", [3,4,3.2], (123, 'john'), {'name': 'john','code':6734}]
        calculator = Calculator()
        for x in range(5) :
            int_exception_raised = False
            non_int_exception_raised = False
            try:
                calculator.ensure_int(integers[x])
            except:
                int_exception_raised = True
            try:
                calculator.ensure_int(non_integers[x])
            except:
                non_int_exception_raised = True
            
            self.assertEqual(False, int_exception_raised, "Exception raised for Integer: " + str(integers[x]))
            self.assertEqual(True, non_int_exception_raised, "No Exception raised for Non-Integer: " + str(non_integers[x]))
        
    # Input Error, Expected Error w/ Negative Dog Food
    def testNegativeDogFood(self):
        calculator = Calculator()
        with self.assertRaises(TypeError) as error:
            calculator.dogfood_calc(small_dogs=5, medium_dogs=5, large_dogs=5, food_supply=-20)
        self.assertEqual(str(error.exception), "unsupported operand type(s) for +: 'int' and 'str'")
    
    # Happy Dog Food Float Path
    def testHappyDogFoodFloat(self):
        calculator = Calculator()
        result = calculator.dogfood_calc(small_dogs=5, medium_dogs=5, large_dogs=5, food_supply=20.9)
        self.assertEqual(result, 334.92, "FAIL: Happy Path for Float Dog Food Input")
    
    # Unit test of number (float or int) check function for dog food
    def testNumberFunction(self):
        numbers = [0, 2000.3, -3, -100.33]
        non_numbers = ["Yolo", [3,4,3.2], (123, 'john'), {'name': 'john','code':6734}]
        calculator = Calculator()
        for x in range(4) :
            number_exception_raised = False
            non_number_exception_raised = False
            try:
                calculator.ensure_number(numbers[x])
            except:
                number_exception_raised = True
            try:
                calculator.ensure_number(non_numbers[x])
            except:
                non_number_exception_raised = True
            
            self.assertEqual(False, number_exception_raised, "Exception raised for Number: " + str(numbers[x]))
            self.assertEqual(True, non_number_exception_raised, "No Exception raised for Non-Number: " + str(non_numbers[x]))