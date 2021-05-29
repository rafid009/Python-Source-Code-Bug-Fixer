import numpy as np 

def function(x):

	z1 = 3
	a6 = x
	x = 0
	paths = []
	try:
		if x <= 9:
			x = x/6
			z1 = a6-a6
			x = 4-x
			paths.append(1)
		else:
			z1 = x*z1
			x = x*x
			x = a6*x
			paths.append(2)
		if x >= 8:
			z1 = z1+8
			x = x+0
			paths.append(3)
		else:
			a6 = a6-a6
			a6 = 4-z1
			z1 = z1-4
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		a6 = z1**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))