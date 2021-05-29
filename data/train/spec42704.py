import numpy as np 

def function(x):

	d6 = 8
	s7 = x
	paths = []
	try:
		if x >= 2:
			s7 = s7*4
			x = 3*x
			x = x-d6
			paths.append(1)
		else:
			d6 = d6*d6
			paths.append(2)
		if d6 <= 9:
			s7 = 8/s7
			paths.append(3)
		else:
			x = 3+s7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))