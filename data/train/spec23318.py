import numpy as np 

def function(x):

	s1 = 7
	l4 = 1
	paths = []
	try:
		if x <= 8:
			s1 = 9+s1
			paths.append(1)
		else:
			x = 3+x
			x = l4*x
			paths.append(2)
		if s1 >= 7:
			l4 = l4*4
			paths.append(3)
		else:
			l4 = l4*l4
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