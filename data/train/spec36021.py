import numpy as np 

def function(x):

	z7 = x
	v8 = 3
	x = x
	paths = []
	try:
		if v8 < 0:
			z7 = z7-4
			paths.append(1)
		else:
			v8 = x+8
			paths.append(2)
		if x <= 1:
			v8 = 5+z7
			v8 = 7+2
			v8 = v8-2
			paths.append(3)
		else:
			x = 5*x
			v8 = 7-v8
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