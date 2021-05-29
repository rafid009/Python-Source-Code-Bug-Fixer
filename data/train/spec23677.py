import numpy as np 

def function(x):

	u7 = 9
	z4 = x
	x = 2
	paths = []
	try:
		if x < 6:
			u7 = u7-7
			x = x-x
			x = 6+9
			paths.append(1)
		else:
			x = x-x
			u7 = u7-x
			paths.append(2)
		if z4 <= 5:
			u7 = 5+8
			u7 = u7+x
			paths.append(3)
		else:
			z4 = 8-z4
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