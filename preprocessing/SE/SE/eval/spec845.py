import numpy as np 

def function(x):

	z6 = x
	j9 = 1
	paths = []
	try:
		if z6 > 7:
			z6 = x+z6
			paths.append(1)
		else:
			z6 = z6-j9
			j9 = j9+x
			paths.append(2)
		if z6 <= 0:
			x = x+x
			paths.append(3)
		else:
			z6 = z6*z6
			z6 = 5+6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))