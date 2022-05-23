from functools import wraps

def greeter(func):
    def decorating(*args, **kwargs):
        name = str(func(*args, **kwargs)).title()
        return 'Aloha ' + name
    return decorating


def sums_of_str_elements_are_equal(func):
    def decorating(*args, **kwargs):
        numbersLst = str(func(*args, **kwargs)).split()
        sign_of_the_number = []
        for i in [int(i) for i in numbersLst]:
            if i>=0:
                sign_of_the_number.append(1)
            else:
                sign_of_the_number.append(-1)

        sum1 = sum([int(n) for n in str(numbersLst[0]) if n.isdigit()])*sign_of_the_number[0]
        sum2 = sum([int(n) for n in str(numbersLst[1]) if n.isdigit()])*sign_of_the_number[1]
        if sum1 == sum2:
            comparison_description = " == "
        else:
            comparison_description = " != "

        return str(sum1) + comparison_description + str(sum2)
    return decorating


def format_output(*required_keys):
    def decorator_function(func_to_be_decorated):
        def decoration(*args, **kwargs):
            result_dict = func_to_be_decorated(*args, **kwargs)

            output_dict = {}
            for key in required_keys:
                output_dict[key] = ""

            for r_key in required_keys:
                temp_list = []
                temp_len = 0
                for sub_key in str(r_key).split("__"):
                    if sub_key in dict(result_dict).keys():
                        temp_len += len(result_dict[sub_key])
                        temp_list.append(result_dict[sub_key])
                    else:
                        raise ValueError("Nope")
                if temp_len == 0:
                    output_dict[r_key] = "Empty value"
                else:
                    output_dict[r_key] = " ".join(temp_list)

            return output_dict
        return decoration
    return decorator_function


def add_method_to_instance(klass):
    def decorator_function(func_to_be_decorated):
        @wraps(func_to_be_decorated)
        def wrapper(self, *args, **kwargs):
            return func_to_be_decorated(*args, **kwargs)
        setattr(klass, func_to_be_decorated.__name__, wrapper)
        return func_to_be_decorated
    return decorator_function
