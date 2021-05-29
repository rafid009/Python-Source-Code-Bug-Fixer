import numpy as np 

def function(x):

	s4 = x
	n1 = 1
	x = x
	paths = []
	try:
		if n1 >= 0:
			s4 = 5/s4
			s4 = s4/s4
			paths.append(1)
		else:
			x = 6/x
			n1 = 1*n1
			paths.append(2)
		if x >= 9:
			s4 = s4-0
			paths.append(3)
		else:
			n1 = n1+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))