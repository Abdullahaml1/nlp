import re

def get_re_expression_grater_than_or_equal(number):
    """
    the function will return an re expressing to search for grater than or
    equal an integer number
    """
    exp = r''
    number_str = str(number)
    for digit in number_str:
        exp += f'[{digit}-9]'

    exp += r'(\.\d*)?'
    exp += f'|(\d{{{len(number_str)+1}}}(\.\d*)?)'
    return exp




exp = get_re_expression_grater_than_or_equal(90)
print(exp)

string = 'this was 100.1 tan'
result = re.search(exp, string)
print(string)
print(result)
print('------------------')

string = 'this was 90 tan'
result = re.search(exp, string)
print(string)
print(result)
print('------------------')


string = 'this was 89 tan'
result = re.search(exp, string)
print(string)
print(result)
print('------------------')
