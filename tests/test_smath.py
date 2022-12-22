from smath import subtract

def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 11
    function.y = 22
    function.z = 33

def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x

### Run to see failed test
# def test_subtract_failed():
#    assert subtract(test_subtract_failed.x) == 12

def test_subtract():
    assert subtract(test_subtract.x) == 10
    assert subtract(test_subtract.y) == 21
    assert subtract(test_subtract.z) == 32

# def test_subtract():
#     assert subtract(10) == 9

#We Can Create More Attributes to functions .. similar to Classes
# def xone():
#     pass 
# xone.x = 11
# xone.y = 22
# xone.z = 33
# print(xone.__dict__)
