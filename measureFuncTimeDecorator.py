import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        score = end - start
        print(score)
    return wrapper

@measure_time
def say_hello(name):
    print("hello", name)
    time.sleep(1)

@measure_time
def say_goodbye():
    print("goodbye")
    time.sleep(4)

say_hello('Kacper')
say_goodbye()
