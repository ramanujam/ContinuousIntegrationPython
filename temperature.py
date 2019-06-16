"""
Convert temperature from fahrenheit to celcius
"""
def convert_temperature(x, conv_type='c2f'):
    if 'int' not in type(x) or 'float' not in type(x):
        raise 'Bad input - please enter integer or fahreinheit'

    if conv_type == 'c2f':
        return c2f(x) 
    elif conv_type == 'f2c':
        return f2c(x)
    else:
        raise "Unsupported Convertion type"

def c2f(x):
    return 9 * x/5 + 32

def f2c(x):
    return (x-32)*5/9

    