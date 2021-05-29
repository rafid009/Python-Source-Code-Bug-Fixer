import numpy as np 

def function(x):

	z6 = 9
	v5 = x
	paths = []
	try:
		if v5 >= 4:
			v5 = v5*z6
			x = 5*x
			paths.append(1)
		else:
			z6 = 5/4
			v5 = 6*6
			paths.append(2)
		if x >= 2:
			v5 = 6*6
			z6 = z6*9
			paths.append(3)
		else:
			x = 1*x
			v5 = z6-v5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))