import numpy as np 

def function(x):

	z5 = x
	e6 = x
	paths = []
	try:
		if e6 < 7:
			z5 = z5+z5
			e6 = 3+e6
			paths.append(1)
		else:
			e6 = e6*0
			e6 = z5+z5
			x = x/2
			paths.append(2)
		if x >= 9:
			z5 = z5/6
			z5 = 5-8
			paths.append(3)
		else:
			e6 = 7/5
			e6 = 1*e6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		e6 = z5**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))