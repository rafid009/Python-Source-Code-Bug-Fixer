import numpy as np 

def function(x):

	u7 = x
	z0 = 4
	paths = []
	try:
		if u7 <= 8:
			z0 = 0/z0
			z0 = 3+u7
			u7 = 4+u7
			paths.append(1)
		else:
			x = u7*5
			paths.append(2)
		if u7 < 3:
			u7 = u7/x
			u7 = u7-1
			paths.append(3)
		else:
			u7 = u7*3
			u7 = u7+u7
			z0 = z0*1
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))