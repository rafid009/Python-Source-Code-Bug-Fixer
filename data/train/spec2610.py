import numpy as np 

def function(x):

	z4 = 3
	u9 = 4
	paths = []
	try:
		if u9 <= 2:
			x = x+x
			z4 = 1-7
			paths.append(1)
		else:
			z4 = z4+2
			paths.append(2)
		if z4 <= 8:
			z4 = 2-z4
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))