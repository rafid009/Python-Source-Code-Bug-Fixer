import numpy as np 

def function(x):

	b3 = x
	z7 = 3
	paths = []
	try:
		if x < 1:
			x = x/9
			b3 = 7*x
			paths.append(1)
		else:
			z7 = b3*z7
			z7 = 4/b3
			paths.append(2)
		if x >= 2:
			b3 = b3+b3
			paths.append(3)
		else:
			z7 = b3*z7
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))