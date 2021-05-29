import numpy as np 

def function(x):

	z4 = x
	i9 = 1
	paths = []
	try:
		if z4 <= 4:
			x = x+x
			x = 8+x
			paths.append(1)
		else:
			z4 = z4-6
			x = 7-z4
			i9 = i9+9
			paths.append(2)
		if z4 < 2:
			z4 = 5/x
			x = x*6
			paths.append(3)
		else:
			z4 = z4*3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		i9 = z4**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))