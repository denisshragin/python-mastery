'''
    In this exercise, you task is this: write a program to answer the following three questions:

    1. How many bus routes exist in Chicago?

    2. How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?

    What is the total number of rides taken on each bus route?

    What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

    You are free to use any technique whatsoever to answer the above questions as long as it's part of 
    
    the Python standard library (i.e., built-in datatypes, standard library modules, etc.).
'''

import readrides


filename = 'Data/ctabus.csv'
rows = readrides.read_rides_as_dicts(filename)

# 1. How many bus routes exist in Chicago?
routes = {row['route'] for row in rows}
number_of_bus_routes = len(routes)
# print(number_of_bus_routes)


# 2. How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?
def get_rides_vs_route_date(route: str, date: str):
    rides = [row['rides'] for row in rows if (row['route']==route and row['date']==date)]
    return rides[0]

# print('How many peoples rode the number 22 bus on February 2, 2011: ', get_rides_vs_route_date('22', '02/02/2011'), '.')

# 3.What is the total number of rides taken on each bus route?
# Count the total number of rides taken with a FOR loop
from pprint import pprint

total_rides = {row['route']: 0 for row in rows}
for row in rows:
    total_rides[row['route']] += row['rides']

# print('The total number of rides taken are:', sorted(total_rides.items()))
# print('--------------------------------------------')

# Count the total number of rides taken with a with Counter class from collections library
from collections import Counter

total_rides_counter = Counter()
for row in rows:
    total_rides_counter[row['route']]+=row['rides']

# print('The total number of rides taken are:')
# pprint(total_rides_counter)
# print('--------------------------------------------')

# 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

def get_n_greatest_increase_in_riderships(rows, n=5, year_1=2001, year_2=2011):
    total_rides_counter_1 = Counter()
    total_rides_counter_2 = Counter()
    for row in rows:
        if int(row['date'][-4:]) == year_1:
            total_rides_counter_1[row['route']] += row['rides'] 
        if int(row['date'][-4:]) == year_2:
            total_rides_counter_2[row['route']] += row['rides'] 
    total_rides_counter_2.subtract(total_rides_counter_1)
    increase_in_ridership = dict(total_rides_counter_2)
    sorted_dict = sorted(increase_in_ridership.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict[:5]

increase_in_ridership_2001_20011 = get_n_greatest_increase_in_riderships(rows=rows, n=5, year_1=2001, year_2=2011)
print("What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?")
for i, item in enumerate(increase_in_ridership_2001_20011):
    print(i+1, ". Bus route:", item[0])
