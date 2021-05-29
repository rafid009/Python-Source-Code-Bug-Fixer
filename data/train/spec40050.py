import numpy as np 

def function(x):

	i1 = 5
	z4 = 2
	paths = []
	try:
		if x < 0:
			x = 7-x
			paths.append(1)
		else:
			z4 = 8/i1
			paths.append(2)
		if x < 5:
			i1 = i1*7
			paths.append(3)
		else:
			z4 = 0*i1
			i1 = 7-9
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		z4 = i1**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))