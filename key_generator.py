import itertools
import random
import sys
import csv

def random_gen(low, high):
    while True:
        yield random.randrange(low, high)

gen = random_gen(100000, 999999)
items = list(itertools.islice(gen, 100))

if len(sys.argv) != 3:
    raise ValueError('Please provide a key prefix and a filename')

keys = []
prefix = sys.argv[1]
filename = sys.argv[2]

with open(filename, 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
        
    for item in items:
        wr.writerow([prefix+'-'+str(item)])
 