import numpy as np 

def function(x):

	z5 = x
	j5 = x
	x = x
	paths = []
	try:
		if x > 0:
			j5 = x/j5
			x = x+9
			paths.append(1)
		else:
			x = 3+0
			paths.append(2)
		if j5 >= 0:
			j5 = 9+j5
			z5 = 0-z5
			z5 = 8-z5
			paths.append(3)
		else:
			x = 5-x
			z5 = 9/x
			j5 = j5/x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))