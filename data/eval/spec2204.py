import numpy as np 

def function(x):

	a3 = 9
	s4 = 6
	x = x
	paths = []
	try:
		if s4 >= 5:
			x = 9-x
			paths.append(1)
		else:
			s4 = 7*s4
			paths.append(2)
		if a3 > 9:
			s4 = 5-0
			paths.append(3)
		else:
			a3 = s4*a3
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