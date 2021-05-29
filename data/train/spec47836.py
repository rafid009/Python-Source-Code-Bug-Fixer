import numpy as np 

def function(x):

	k2 = 7
	z6 = x
	paths = []
	try:
		if x > 0:
			x = 0-x
			x = x+7
			x = x+k2
			paths.append(1)
		else:
			x = x+7
			z6 = x/8
			paths.append(2)
		if x <= 7:
			k2 = 5+x
			k2 = k2+4
			k2 = k2*2
			paths.append(3)
		else:
			x = 2*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))