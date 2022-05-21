def greeter(func):
    def decorating():
        return 'Aloha ' + func()
    return decorating


def sums_of_str_elements_are_equal(func):
    def decorating():
        numbersLst = str(func()).split()
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
    pass


def add_method_to_instance(klass):
    pass
