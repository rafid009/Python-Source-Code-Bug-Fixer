import numpy as np 

def function(x):

	s6 = x
	d0 = x
	x = x
	paths = []
	try:
		if x <= 2:
			s6 = 5+s6
			s6 = 6*4
			paths.append(1)
		else:
			x = 8*x
			x = s6+x
			paths.append(2)
		if x > 9:
			d0 = 1-0
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))