import numpy as np 

def function(x):

	z8 = 2
	j0 = 7
	paths = []
	try:
		if j0 > 0:
			j0 = j0/5
			z8 = 1-z8
			paths.append(1)
		else:
			z8 = z8*9
			paths.append(2)
		if z8 > 6:
			j0 = 1*2
			paths.append(3)
		else:
			z8 = j0/5
			j0 = x/1
			j0 = 9-j0
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