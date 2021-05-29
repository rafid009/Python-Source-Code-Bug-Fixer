import numpy as np 

def function(x):

	a8 = x
	z1 = 1
	paths = []
	try:
		if x >= 2:
			a8 = a8+5
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if z1 > 3:
			z1 = x/5
			x = 2+x
			paths.append(3)
		else:
			z1 = 3*7
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))