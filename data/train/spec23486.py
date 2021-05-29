import numpy as np 

def function(x):

	n6 = 8
	s1 = x
	x = x
	paths = []
	try:
		if s1 > 5:
			n6 = x+n6
			paths.append(1)
		else:
			s1 = n6/9
			paths.append(2)
		if n6 <= 8:
			s1 = x*n6
			x = x+5
			paths.append(3)
		else:
			x = x*x
			s1 = 1-s1
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