import numpy as np 

def function(x):

	z5 = x
	a1 = 5
	paths = []
	try:
		if a1 >= 2:
			a1 = 2/7
			a1 = 9+1
			x = 3+5
			paths.append(1)
		else:
			z5 = a1-z5
			paths.append(2)
		if x > 4:
			a1 = a1*x
			paths.append(3)
		else:
			x = 9-6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))