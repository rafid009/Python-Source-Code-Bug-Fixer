import numpy as np 

def function(x):

	s6 = 4
	n7 = 0
	paths = []
	try:
		if x < 1:
			n7 = n7-6
			s6 = 8+s6
			paths.append(1)
		else:
			n7 = 6-n7
			paths.append(2)
		if x < 0:
			n7 = n7-9
			x = 9*x
			n7 = n7+x
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))