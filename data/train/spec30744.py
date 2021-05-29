import numpy as np 

def function(x):

	z8 = x
	i7 = 0
	paths = []
	try:
		if i7 > 2:
			x = 9/x
			z8 = 2+z8
			i7 = 1/4
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if z8 <= 7:
			x = 1*5
			x = x+6
			z8 = z8*7
			paths.append(3)
		else:
			i7 = i7*4
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))