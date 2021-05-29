import numpy as np 

def function(x):

	s6 = 6
	n6 = x
	paths = []
	try:
		if n6 >= 2:
			n6 = n6*s6
			paths.append(1)
		else:
			s6 = s6*x
			paths.append(2)
		if x > 7:
			x = 7+3
			paths.append(3)
		else:
			x = x-5
			n6 = 0-0
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		n6 = s6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))