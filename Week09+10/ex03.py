import time

def timer(func):
   
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(end_time-start_time)
    return inner

@timer
def test():
    time.sleep(3)

@timer
def test2(a,b):
    time.sleep(a)
    print(a+b)

test()

test2(2,10000)



