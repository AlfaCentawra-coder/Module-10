import datetime
from multiprocessing import Pool

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline().strip()
        while line:
            all_data.append(line)
            line = f.readline().strip()


#start_time = datetime.datetime.now()
#if __name__ == '__main__':
#    with Pool() as pool:
#        result = pool.map(read_info, files)
#    end_time = datetime.datetime.now()
#    execution_time = end_time - start_time
#    print(f"Multiprocessing Execution Time: {execution_time}")

start_time = datetime.datetime.now()
for file in files:
    read_info(file)
    end_time = datetime.datetime.now()
print(end_time - start_time)







