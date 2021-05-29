import numpy as np 

def function(x):

	z1 = 9
	q4 = 2
	paths = []
	try:
		if z1 > 7:
			q4 = 9+q4
			paths.append(1)
		else:
			x = x+z1
			paths.append(2)
		if x < 1:
			q4 = q4*x
			z1 = 2-x
			paths.append(3)
		else:
			q4 = 5-2
			x = q4+6
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))