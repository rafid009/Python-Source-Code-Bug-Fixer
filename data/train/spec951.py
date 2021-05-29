import numpy as np 

def function(x):

	n1 = x
	z1 = x
	paths = []
	try:
		if x > 3:
			x = x*z1
			paths.append(1)
		else:
			x = 5+x
			z1 = 0*x
			paths.append(2)
		if n1 >= 0:
			x = 7/7
			paths.append(3)
		else:
			x = 4*5
			x = 8-6
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))