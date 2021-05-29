import numpy as np 

def function(x):

	e6 = x
	z8 = x
	paths = []
	try:
		if e6 <= 1:
			z8 = x+9
			paths.append(1)
		else:
			e6 = e6/8
			z8 = z8-x
			e6 = 7+x
			paths.append(2)
		if x >= 3:
			e6 = z8+1
			paths.append(3)
		else:
			z8 = z8*4
			e6 = 1*e6
			z8 = e6+z8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		e6 = z8**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))