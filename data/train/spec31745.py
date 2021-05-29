import numpy as np 

def function(x):

	e7 = x
	z8 = x
	paths = []
	try:
		if x > 9:
			x = z8+x
			e7 = 7-e7
			x = x*z8
			paths.append(1)
		else:
			z8 = 7*z8
			x = x/8
			paths.append(2)
		if z8 > 7:
			z8 = 7*9
			paths.append(3)
		else:
			e7 = e7/9
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		e7 = z8**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))