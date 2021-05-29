import numpy as np 

def function(x):

	s4 = 8
	d8 = x
	paths = []
	try:
		if d8 < 1:
			s4 = s4-d8
			d8 = d8+3
			s4 = 4/s4
			paths.append(1)
		else:
			s4 = s4/x
			d8 = d8/3
			paths.append(2)
		if s4 >= 9:
			s4 = s4/6
			d8 = d8/x
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))