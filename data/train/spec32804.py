import numpy as np 

def function(x):

	z1 = 7
	j5 = x
	paths = []
	try:
		if x >= 3:
			j5 = j5+1
			z1 = 5/j5
			z1 = j5-6
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if x <= 2:
			j5 = 4-z1
			paths.append(3)
		else:
			z1 = z1/x
			z1 = z1+7
			j5 = 1/j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		z1 = j5**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))