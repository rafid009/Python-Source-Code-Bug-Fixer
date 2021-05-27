import numpy as np 

def function(x):

	a6 = 8
	z9 = 9
	paths = []
	try:
		if a6 >= 8:
			a6 = z9-a6
			paths.append(1)
		else:
			z9 = a6-3
			x = x/z9
			paths.append(2)
		if z9 >= 8:
			a6 = 1-a6
			z9 = z9/3
			a6 = 5*x
			paths.append(3)
		else:
			a6 = 3+a6
			a6 = a6*1
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))