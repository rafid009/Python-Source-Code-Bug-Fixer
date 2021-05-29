import numpy as np 

def function(x):

	j0 = 7
	z9 = 3
	paths = []
	try:
		if z9 >= 2:
			j0 = x/j0
			j0 = x-j0
			j0 = 3+j0
			paths.append(1)
		else:
			j0 = 8-j0
			paths.append(2)
		if j0 >= 5:
			z9 = z9+5
			z9 = 1/j0
			paths.append(3)
		else:
			z9 = z9/x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))