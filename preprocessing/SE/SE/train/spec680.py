import numpy as np 

def function(x):

	d4 = x
	z7 = 2
	paths = []
	try:
		if d4 <= 9:
			x = x-9
			paths.append(1)
		else:
			d4 = 3-3
			x = x-z7
			d4 = d4/6
			paths.append(2)
		if d4 < 6:
			x = x-7
			z7 = x+5
			z7 = z7+4
			paths.append(3)
		else:
			x = 6+x
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