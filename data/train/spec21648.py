import numpy as np 

def function(x):

	a3 = x
	z5 = x
	paths = []
	try:
		if a3 <= 9:
			x = z5-8
			x = 1*z5
			x = x/3
			paths.append(1)
		else:
			z5 = 4-z5
			paths.append(2)
		if z5 > 1:
			x = x/a3
			paths.append(3)
		else:
			x = x-a3
			a3 = a3*a3
			z5 = z5-9
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		a3 = z5**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))