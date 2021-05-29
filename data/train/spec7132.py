import numpy as np 

def function(x):

	z6 = x
	v1 = x
	paths = []
	try:
		if v1 >= 1:
			v1 = 1+7
			v1 = v1-z6
			v1 = v1+2
			paths.append(1)
		else:
			x = z6*x
			paths.append(2)
		if v1 >= 4:
			z6 = 7/x
			v1 = v1*1
			paths.append(3)
		else:
			z6 = x*z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))