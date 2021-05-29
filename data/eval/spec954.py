import numpy as np 

def function(x):

	x2 = 7
	z6 = 5
	paths = []
	try:
		if x2 > 0:
			x = x2-x
			z6 = 3+z6
			paths.append(1)
		else:
			x = 7*0
			x = 8+1
			paths.append(2)
		if x > 0:
			x = 5-x
			paths.append(3)
		else:
			x = x-3
			x2 = x+7
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))