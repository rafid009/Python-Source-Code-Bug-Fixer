import numpy as np 

def function(x):

	z7 = x
	b0 = x
	paths = []
	try:
		if b0 <= 0:
			z7 = z7-0
			z7 = z7/3
			z7 = 3-3
			paths.append(1)
		else:
			b0 = 7-b0
			x = x+5
			paths.append(2)
		if x < 0:
			x = x-9
			x = 3-6
			z7 = x*4
			paths.append(3)
		else:
			z7 = z7/b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))