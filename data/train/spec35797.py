import numpy as np 

def function(x):

	z4 = 8
	v8 = x
	paths = []
	try:
		if x > 6:
			x = v8/2
			x = z4+6
			paths.append(1)
		else:
			v8 = 0-1
			x = 5+x
			paths.append(2)
		if z4 <= 3:
			z4 = z4+4
			paths.append(3)
		else:
			x = v8-6
			x = x/4
			v8 = v8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))