import numpy as np 

def function(x):

	z1 = 3
	j7 = 5
	paths = []
	try:
		if x < 8:
			j7 = 0+j7
			j7 = j7+7
			z1 = x/z1
			paths.append(1)
		else:
			j7 = 6+j7
			paths.append(2)
		if z1 <= 8:
			x = 5*x
			z1 = z1*2
			paths.append(3)
		else:
			x = j7+4
			j7 = z1*x
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))