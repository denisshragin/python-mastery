import tracemalloc

filepath = 'Data/ctabus.csv'

def read_all_data(filepath): 
    print("Read the entire file into one string:")
    f = open(filepath)
    tracemalloc.start()
    data = f.read()
    print("Len data: ", len(data))
    current, peak = tracemalloc.get_traced_memory()
    current, peak = current//(1024*1024), peak//(1024*1024)
    print("Current: ", current, ' Mb')
    print("Peak: ", peak, ' Mb')
    f.close()
    print("-------------------------\n")

def read_list_of_strings(filepath):
    print("Read the entire file into a list of strings:")
    f = open(filepath)
    tracemalloc.start()
    lines = f.readlines()
    print("Len data: ", len(lines))
    current, peak = tracemalloc.get_traced_memory()
    print("Current: ", current)
    print("Peak: ", peak)
    f.close()
    print("-------------------------\n")





read_all_data(filepath)

read_list_of_strings(filepath)