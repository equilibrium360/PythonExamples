"""Lambda function examples
"""

"""Example 1
"""
print('EXAMPLE 1')
sum5 = lambda x: x+5
print(sum5(7))

"""Sorting a list of Tuples using lambda
"""
print('Sorting a list of tuples using lambda')
list1 = [('eggs', 5.25), ('honey', 4.57), ('carrots', 87.8), ('peaches', 56.4)]
list1.sort(key = lambda x: x[1] )
print(list1)


"""Sorting a list of Dictionaries using lambda
"""
print('\n\nSorting a list of dictionaries using lambda')

import pprint as pp
car_list = [
        {'make':'toyota', 'model':'rav4', 'year':2019}, 
        {'make':'lexus', 'model':'nx300', 'year':2018}, 
        {'make':'subaru', 'model':'forrester', 'year':2020} 
        ]

sorted_car_list = sorted(car_list, key =lambda x: x['year'] )

pp.pprint(sorted_car_list)

"""Filter example using lambdas
"""
print('Filter example using lambdas')
num_list = [1,2,3,4,5,6,7,8,9,0]
flist = list(filter(lambda x: x%2 == 0, num_list))
print(flist)

print('using map function')
sqr = list(map(lambda x: x*x, num_list))
print(sqr)



