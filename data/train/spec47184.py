import numpy as np 

def function(x):

	t6 = x
	z8 = 7
	paths = []
	try:
		if z8 <= 6:
			z8 = 1*5
			paths.append(1)
		else:
			z8 = x-8
			t6 = t6/5
			paths.append(2)
		if t6 >= 6:
			t6 = 3*t6
			z8 = t6-x
			paths.append(3)
		else:
			x = 4+x
			x = t6*x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))