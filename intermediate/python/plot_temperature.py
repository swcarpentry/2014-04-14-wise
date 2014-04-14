import numpy as np
from matplotlib import pyplot

def read_csv_file(filename):
    '''
    This code will read in a CSV file of year, temperature, rainfall, and number of mosquitos and return 4 arrays, one for each column
    '''
    assert isinstance(filename, str), 'filename must be a string'
    year, temperature, rainfall, mosquitos = np.genfromtxt(filename, skiprows = 1, delimiter = ',', unpack = True)
    return year, temperature, rainfall, mosquitos

def convert_fahrenheit_to_celsius(temp_in_f):
    '''
    This code will convert an array of tempertures from fahrenheit to celsius
    '''
    assert isinstance(temp_in_f, float) or isinstance(temp_in_f, int), 'temperature must be an int or float'
    temp_in_c = (temp_in_f - 32) * 5 / 9.0
    return temp_in_c
    
def plot_data(x, y, symbol = 'o'):
    pyplot.plot(x, y, symbol)
    pyplot.savefig('temp_vs_mosquitos.pdf')
    pyplot.close()
    
    
if __name__ == "__main__":
	year, temperature, rainfall, mosquitos = read_csv_file('mosquito_data_A1.csv')
	temp_in_c = convert_fahrenheit_to_celsius(temperature)
	plot_data()