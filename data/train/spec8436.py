import numpy as np 

def function(x):

	x7 = x
	z4 = 3
	paths = []
	try:
		if z4 < 9:
			z4 = z4*2
			x = x+7
			x7 = x/x7
			paths.append(1)
		else:
			x = x*2
			x7 = x7*9
			paths.append(2)
		if z4 <= 6:
			x = 2-x
			x7 = 0-x7
			paths.append(3)
		else:
			x = x-0
			x7 = x7+3
			x7 = 3/4
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))