import numpy as np 

def function(x):

	c3 = 9
	z9 = 2
	paths = []
	try:
		if c3 >= 6:
			z9 = c3*z9
			z9 = 6*z9
			paths.append(1)
		else:
			x = x/x
			x = x/z9
			x = 2+c3
			paths.append(2)
		if c3 < 1:
			x = 5+c3
			paths.append(3)
		else:
			c3 = 1-9
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		z9 = c3**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))