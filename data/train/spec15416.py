import numpy as np 

def function(x):

	n8 = 3
	s4 = 3
	paths = []
	try:
		if n8 >= 6:
			n8 = 4*n8
			n8 = s4-8
			x = x*3
			paths.append(1)
		else:
			n8 = n8-x
			paths.append(2)
		if s4 > 8:
			x = x*7
			s4 = s4+9
			paths.append(3)
		else:
			s4 = s4*3
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