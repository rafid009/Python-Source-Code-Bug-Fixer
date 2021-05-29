import numpy as np 

def function(x):

	y3 = x
	z6 = 8
	paths = []
	try:
		if y3 > 4:
			x = x-0
			paths.append(1)
		else:
			z6 = 5-1
			paths.append(2)
		if z6 > 4:
			x = x-5
			x = y3*x
			paths.append(3)
		else:
			x = x*0
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		z6 = y3**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))