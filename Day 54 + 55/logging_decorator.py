def logging_decorator(function):
    def wrapper_function(*args):
        string = function.__name__
        for i in range(len(args)):
            string += f"\nArg {i+1}: {args[i]}"
        print(string)
    return wrapper_function


@logging_decorator
def test_function(name, age, year, number):
    pass


test_function("Johnny", "19", "2022", 15)
            