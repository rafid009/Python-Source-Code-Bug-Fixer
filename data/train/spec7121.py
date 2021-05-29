import numpy as np 

def function(x):

	z7 = 6
	f7 = 3
	paths = []
	try:
		if f7 <= 6:
			z7 = 8+z7
			paths.append(1)
		else:
			f7 = 2-f7
			z7 = 5+z7
			paths.append(2)
		if z7 < 8:
			f7 = f7/6
			paths.append(3)
		else:
			x = x*4
			z7 = 9*2
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))