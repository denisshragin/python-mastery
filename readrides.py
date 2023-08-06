import csv
from collections import namedtuple

filename = 'Data/ctabus.csv'


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class Row_with_slots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def print_current_peak(current, peak):
    current, peak = current//(1024*1024), peak//(1024*1024)
    print("Current: ", current, ' Mb')
    print("Peak: ", peak, ' Mb')
    print("-------------------------\n")


def read_all_data(filename): 
    print("Read the entire file into one string:")
    f = open(filename)
    tracemalloc.start()
    data = f.read()
    print("Len data: ", len(data))
    current, peak = tracemalloc.get_traced_memory()
    print_current_peak(current, peak)
    f.close()
    print("-------------------------\n")


def read_list_of_strings(filename):
    print("Read the entire file into a list of strings:")
    f = open(filename)
    tracemalloc.start()
    lines = f.readlines()
    print("Len data: ", len(lines))
    current, peak = tracemalloc.get_traced_memory()
    print_current_peak(current, peak)
    f.close()
    print("-------------------------\n")


def read_rides_as_tuples(filename):
    '''
    Read the bus rides data as a list of tuples    
    '''
    records = []
    print("-------------------------\n")
    print("Read the entire file into a list of tuples: ")
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    '''
    Read the bus rides data as a list of dicts    
    '''
    print("-------------------------\n")
    print("Read the entire file into a list of dicts: ")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records


def read_rides_as_instances(filename):
    '''
    Read the bus rides data as a list of objects of a Row class  
    '''
    print("-------------------------\n")
    print("Read the entire file into a list of instances: ")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_named_tuples(filename):
    '''
    Read the bus rides data as a list of named tuples   
    '''
    print("-------------------------\n")
    print("Read the entire file into a list of named tuples: ")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            Row = namedtuple('Row', ('route', 'date', 'daytype', 'rides'))
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_objects_with_slots(filename):
    '''
    Read the bus rides data as a list of objects of a Row class with slots 
    '''
    print("-------------------------\n")
    print("Read the entire file into a list of instances (class Row with slots): ")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row_with_slots(route=route, date=date, daytype=daytype, rides=rides)
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    # read_all_data(filename=filename)
    # read_list_of_strings(filename=filename)
    
    tracemalloc.start()
    rows = read_rides_as_named_tuples(filename)
    current, peak = tracemalloc.get_traced_memory()
    print_current_peak(current, peak)
