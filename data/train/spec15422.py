import numpy as np 

def function(x):

	z7 = 5
	v6 = 1
	paths = []
	try:
		if x > 2:
			v6 = v6-9
			v6 = v6-8
			paths.append(1)
		else:
			v6 = 3+v6
			z7 = 1-8
			x = x/8
			paths.append(2)
		if x <= 9:
			v6 = 6/v6
			v6 = v6*9
			paths.append(3)
		else:
			v6 = v6-z7
			v6 = v6*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))