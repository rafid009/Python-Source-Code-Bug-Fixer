import numpy as np 

def function(x):

	s4 = 5
	x3 = 9
	paths = []
	try:
		if x > 5:
			s4 = 8+s4
			s4 = x*9
			x3 = x+s4
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if x < 9:
			s4 = 2-s4
			paths.append(3)
		else:
			x3 = 2-x3
			x = x+4
			x3 = x3*6
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		s4 = x3**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))