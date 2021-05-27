import numpy as np 

def function(x):

	a1 = x
	z1 = 6
	paths = []
	try:
		if x < 6:
			x = x+2
			paths.append(1)
		else:
			z1 = z1*z1
			paths.append(2)
		if a1 < 0:
			z1 = z1-9
			paths.append(3)
		else:
			x = z1*x
			x = x/6
			a1 = 4/a1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))