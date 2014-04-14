import plot_temperature
import numpy as np
def test_output_read_csv_file():
    year, temperature, rainfall, mosquitos = plot_temperature.read_csv_file('mosquito_data_A1.csv')
    assert (year == np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010])).all()
    
def test_convert_fahrenheit_to_celsius():
    temp_c = plot_temperature.convert_fahrenheit_to_celsius(32)
    assert temp_c == 0, '32F != 0C'
