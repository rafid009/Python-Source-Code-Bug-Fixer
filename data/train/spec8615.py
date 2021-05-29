import numpy as np 

def function(x):

	z9 = 0
	e7 = 3
	paths = []
	try:
		if x >= 3:
			z9 = z9-5
			z9 = 1+0
			paths.append(1)
		else:
			x = 6/x
			x = 2-6
			e7 = x+e7
			paths.append(2)
		if x > 2:
			e7 = 5/z9
			e7 = 2+x
			paths.append(3)
		else:
			z9 = x-z9
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))