import numpy as np 

def function(x):

	z6 = 1
	j2 = 2
	paths = []
	try:
		if x > 8:
			j2 = z6+1
			x = x+0
			paths.append(1)
		else:
			z6 = 3*j2
			z6 = 4*z6
			j2 = 8/j2
			paths.append(2)
		if x >= 9:
			z6 = 7-9
			paths.append(3)
		else:
			j2 = 2*j2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))