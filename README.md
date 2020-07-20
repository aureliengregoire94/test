# Test scraping python
## Before starting
 * Fork the project in your namespace
 * **Caution! very important:** Change project visibility: 
   * Click on `Settings` bottom left, when you see your project 
   * Select `General`
   * Click on expend `Visibility, project features, permissions` 
   * Change project visibility from public to private
## After pushing your codes
 * Add it@dataimpact.fr as **reporter** in `members`
 * Answer the email with your project link in it 
 
# Test
Some really important tips:
 * Comments and automated tests are a big plus
 * You might need pytest (and you can use any other package)
 * There are three parts (algorithm, advanced, scraping) you can choose to skip one.
 * You can use internet
 

## First Part (python algorithm)

### Exercise 1
In the function exercise_one on first_part.src module:
print every number between 1 and 100 as follows:
 * For every multiple of 3 print "Three".
 * For every multiple of 5 print "Five".
 * And for every multiple of both 3 and 5 print "ThreeFive"

*The output should be as follows:*

```
1
2
Three
4
Five
Three
7
8
Three
Five
11
Three
13
14
ThreeFive
16
```

### Exercise 2 (15 min)
Find the Missing Number

You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

Examples:
```
Input: arr = [8, 2, 3, 6, 4, 7, 1] --> Output: 5

Input: arr = [2, 1, 3, 5] --> Output: 4
```

### Exercise 3 (10 min)

Write a function calculate that takes a list of strings a returns the sum of the list items that represents an integer (skipping the other items).
Examples
```
calculate(['4', '3', '-2']) ➞ 5
calculate(453) ➞ False
calculate(['nothing', 3, '8', 2, '1']) ➞ 9
calculate('54') ➞ False
```

### Exercise 4 (25 min)
Sort an array without changing position of negative numbers

Given an array arr[] of N integers, the task is to sort the array without changing the position of negative numbers (if any) i.e. the negative numbers need not be sorted.
Examples:

```
Input: arr = [2, -6, -3, 8, 4, 1] --> Output: 1 -6 -3 2 4 8

Input: arr = [-2, -6, -3, -8, 4, 1] --> Output: -2 -6 -3 -8 1 4
```

## Second Part (python advanced)

### Exercise 1 (5 min)

Make the test `test_my_set` work by implementing the class `MySet` (you don't have to change anything on the test part for this exercise)

### Exercise 2 (10 min)

Rewrite decorator_check_max_int to force the function "add" not to return values greater than maxsize

### Exercise 3 (10 min)

Rewrite `ignore_exception` so that it ignores the exception in its argument and returns None if this exception raises

### Exercise 4 (20 min)

Write the tests for the class `CacheDecorator` without touching it, some of your tests should not pass because this class is a little buggy. 

### Exercise 5 (10 min)

Write the metaclass `MetaInherList` so that the class `ForceToList` inherits from `list` built-in. (read `test_meta_list` in the tests for more information)

### Exercise 6 (15 min)
Create a metaclass that checks if classes have an attribute named 'process' which must be a method taking 3 arguments

## Third Part (scraping)

### Exercise 1 (5 min)
Create a function http_request that sends a post request to this url https://httpbin.org/anything with this parameters:
```msg=welcomeuser
isadmin=1
```
and return the response body.
Now, send the same request this time by changing the user-agent

### Exercise 2 (20 min)
In src module, create a python class with the following constraints:
  * it imports the data.json.gz file which is located in the third_part/data folder. The file holds information about a category including the products.
  * it prints each available product in this particular format:
“You can buy Product_Name at our store at Product_Price”
where :
    - Product_Name is the product name truncated at 30 .
    - Abbotts Village Bakery Ghrainy Wolemeal 850g ==> Abbotts Village Bakery Grainy
    - Product_Price is the rounded product price in dd.d format
    - Example: 13.34 ==> 13.3

  * if the product is unavailable, it logs the product id and product name.
  * if a clue of the product’s availability can’t be found, it logs an error.
  * it saves the available products in a csv file.
###### P.S :

  * Use any tool/language/method/website to find the products in the json file.
  * To "truncate" means "to shorten by cutting off the top or end".

### Exercise 3 (35 min)
In the third_part folder, start a new scrapy project and build a spider that crawls the webpage below,
extracting the products names, and the breadcrumb in a list format. Make sure to take
advantage of Scrapy.Items to output the products.
Test your spider and save the results in a csv file.
Webpage:
```
https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas
```
Breadcrumb :
```
Home > Drinks > Cordials, Juices & Iced Teas > Iced Teas
```
The desired format:
```
[“Home”, “Drinks”, “Cordials, Juices & Iced Teas”, “ Iced Teas”]
```
