# Guild - QA Engineer Project for **Chris Luhring** #
*11/13/2020*

This PyDev project was prepared using unittest on Eclipse. The tests live in TestDogShelter.py, which test the Calculator Class in calculator.py.  I ran the tests in Eclipse, but was also able to run them from the command line, like so:

PythonDogShelterTest\src>python -m unittest -v dogshelter.test.TestDogShelter

**Hypothetical**: You are the owner of a dog shelter that can hold at most 30 dogs. You want
a programmatic way to order the necessary amount of food for next month based on how
many dogs you currently have and the remaining food from last month.
Sizes of dogs and food needs:
* Small - 10lbs.,
* Medium - 20lbs.,
* Large - 30lbs.

When ordering food you always want to order at least 20% more than the minimum needed
to feed all dogs currently in your shelter for that month.
**Example**:
If at the end of the month I have 5 small dogs, 3 medium dogs, 7 large dogs, and a leftover
food supply of 17lbs. I should expect the function would tell me to order 363.6 lbs.

## Cases not covered in AC:
* days in a month February w/ 28 or 29 days vs. January w/ 31 days
* dogs get adopted from shelters, change in dogs affects food consumption
* pounds & ounces are not easily [converted]( https://support.mightymerchant.com/ounces-to-decimal-conversion-chart "Title") to decimals
* classification of small, medium, large dogs is subjective - not specified
* not all dogs eat the same, eg. sick dogs
