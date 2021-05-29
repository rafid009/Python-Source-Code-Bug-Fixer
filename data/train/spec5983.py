import numpy as np 

def function(x):

	v6 = x
	z0 = x
	x = x
	paths = []
	try:
		if z0 <= 8:
			x = x*3
			paths.append(1)
		else:
			z0 = z0-z0
			z0 = z0-z0
			x = v6-0
			paths.append(2)
		if v6 <= 3:
			v6 = v6*9
			z0 = 2+0
			v6 = 5*x
			paths.append(3)
		else:
			z0 = z0-5
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))