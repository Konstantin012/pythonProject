
def decorator1 (func ):
    def wrapper(*args, **kwargs):
        print("before func1")
        func(*args, **kwargs)
        print("after func1")
    return wrapper

def decorator2 (func):
    def wrapper(*args, **kwargs):
        print("before func2")
        func(*args, **kwargs)
        print("after func2")
    return wrapper

@decorator1
@decorator2
def test(name):
    print("z nen", name)

test("good")

# test= decorator(test)
# test("good")
