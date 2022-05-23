def greeter(func):
    def decorating(*args, **kwargs):
        name = str(func(*args, **kwargs)).title()
        return 'Aloha ' + name
    return decorating


def sums_of_str_elements_are_equal(func):
    def decorating(*args, **kwargs):
        numbersLst = str(func(*args, **kwargs)).split()
        sign_of_the_number = [np.sign(i) for i in [int(i) for i in numbersLst]]

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
        def decoration():
            result_dict = func_to_be_decorated()

            output_dict = {}
            for r_key in required_keys:
                temp_list = []
                for sub_key in str(r_key).split("__"):
                    if sub_key in dict(result_dict).keys():
                        temp_list.append(result_dict[sub_key])
                    else:
                        raise ValueError("Nope")
                output_dict[r_key] = " ".join(temp_list)

            return output_dict
        return decoration
    return decorator_function


def add_method_to_instance(klass):
    pass
