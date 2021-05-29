import numpy as np 

def function(x):

	z5 = x
	s5 = 4
	paths = []
	try:
		if x > 4:
			z5 = 8-z5
			x = x*1
			s5 = 8+9
			paths.append(1)
		else:
			s5 = 7*7
			x = 6/z5
			paths.append(2)
		if x >= 6:
			x = 6-x
			z5 = z5-z5
			paths.append(3)
		else:
			x = 2-4
			x = s5-z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))