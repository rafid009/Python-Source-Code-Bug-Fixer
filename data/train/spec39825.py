import numpy as np 

def function(x):

	s4 = 3
	y5 = x
	paths = []
	try:
		if x <= 4:
			x = x/2
			s4 = x+2
			paths.append(1)
		else:
			y5 = y5-x
			paths.append(2)
		if y5 >= 1:
			x = x*y5
			paths.append(3)
		else:
			s4 = 9-s4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))