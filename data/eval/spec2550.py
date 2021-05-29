import numpy as np 

def function(x):

	u4 = x
	z8 = 3
	x = 3
	paths = []
	try:
		if u4 >= 5:
			u4 = u4*3
			x = 4/x
			x = 2*x
			paths.append(1)
		else:
			z8 = z8+4
			z8 = u4*z8
			u4 = 5/9
			paths.append(2)
		if z8 >= 8:
			u4 = 8-u4
			paths.append(3)
		else:
			u4 = u4+1
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))