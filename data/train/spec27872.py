import numpy as np 

def function(x):

	q7 = 4
	z4 = 3
	paths = []
	try:
		if x > 0:
			q7 = 2/q7
			paths.append(1)
		else:
			q7 = q7*6
			x = 0+x
			paths.append(2)
		if x < 4:
			x = x+x
			q7 = 5+q7
			x = 5-x
			paths.append(3)
		else:
			z4 = 9*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))