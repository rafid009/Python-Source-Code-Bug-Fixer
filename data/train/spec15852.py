import numpy as np 

def function(x):

	i2 = 1
	z7 = x
	paths = []
	try:
		if i2 >= 7:
			x = 3/5
			z7 = z7+x
			paths.append(1)
		else:
			i2 = i2-3
			i2 = i2/7
			z7 = z7-3
			paths.append(2)
		if i2 <= 2:
			i2 = 7+i2
			i2 = x/i2
			paths.append(3)
		else:
			z7 = 9-z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))