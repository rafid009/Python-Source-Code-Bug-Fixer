import numpy as np 

def function(x):

	i2 = 3
	z7 = x
	paths = []
	try:
		if x >= 3:
			z7 = x/z7
			paths.append(1)
		else:
			i2 = i2-3
			i2 = 7*6
			paths.append(2)
		if z7 <= 2:
			i2 = i2-4
			paths.append(3)
		else:
			z7 = 8*z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		i2 = z7**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))