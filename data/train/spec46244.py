import numpy as np 

def function(x):

	d1 = x
	s4 = x
	paths = []
	try:
		if d1 <= 7:
			s4 = 4/s4
			x = x/2
			s4 = s4/6
			paths.append(1)
		else:
			d1 = 1-d1
			x = 6*x
			paths.append(2)
		if d1 > 6:
			x = 6+8
			x = x-x
			paths.append(3)
		else:
			x = 5*x
			d1 = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))