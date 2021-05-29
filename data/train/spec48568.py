import numpy as np 

def function(x):

	s2 = x
	n1 = 9
	paths = []
	try:
		if x >= 4:
			n1 = n1*0
			n1 = 3*n1
			s2 = 8-9
			paths.append(1)
		else:
			x = 8-x
			s2 = 9*x
			paths.append(2)
		if x >= 8:
			x = 2-3
			s2 = 1/s2
			x = n1-4
			paths.append(3)
		else:
			n1 = 7*n1
			n1 = 9*n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))