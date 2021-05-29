import numpy as np 

def function(x):

	n6 = 9
	s1 = 4
	paths = []
	try:
		if n6 >= 8:
			n6 = n6*n6
			paths.append(1)
		else:
			n6 = 1-7
			x = 0-n6
			n6 = 3*7
			paths.append(2)
		if x <= 5:
			s1 = s1+0
			paths.append(3)
		else:
			x = x*5
			x = x*s1
			s1 = x/s1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))