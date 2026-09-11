import time

start = time.time()
# Code whose execution time you want to measure
end = time.time()


# better one : more precise
start = time.perf_counter()
# Code
end = time.perf_counter()

time_taken = end - start
print("Execution time:", time_taken, "seconds")


'''

import time

def timer(func):

    def wrapper():
    
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print("Execution time:", end - start)

    return wrapper


@timer
def hello():
    # code

hello()


'''