import numpy as np 

def function(x):

	z6 = 9
	v6 = x
	paths = []
	try:
		if v6 > 0:
			x = 0/z6
			v6 = v6-4
			z6 = 4+v6
			paths.append(1)
		else:
			v6 = v6+2
			paths.append(2)
		if v6 < 7:
			x = x*x
			x = x-z6
			paths.append(3)
		else:
			z6 = v6*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))