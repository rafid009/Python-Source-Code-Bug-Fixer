import numpy as np 

def function(x):

	z5 = 0
	j7 = 6
	paths = []
	try:
		if j7 <= 6:
			j7 = 7+j7
			j7 = j7/6
			paths.append(1)
		else:
			j7 = j7+9
			j7 = j7+z5
			j7 = z5*5
			paths.append(2)
		if j7 >= 3:
			z5 = 0/z5
			x = z5*x
			paths.append(3)
		else:
			j7 = j7/x
			z5 = z5-5
			j7 = j7+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))