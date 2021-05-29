import numpy as np 

def function(x):

	u3 = 8
	z4 = 7
	paths = []
	try:
		if x >= 6:
			u3 = u3*9
			z4 = z4-x
			paths.append(1)
		else:
			u3 = 9/u3
			u3 = z4*0
			paths.append(2)
		if x > 2:
			x = u3-u3
			paths.append(3)
		else:
			x = 5/x
			x = 4*x
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