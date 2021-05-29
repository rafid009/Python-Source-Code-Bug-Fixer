import numpy as np 

def function(x):

	z5 = x
	b6 = x
	x = 3
	paths = []
	try:
		if x < 7:
			z5 = 5/7
			x = 7+b6
			paths.append(1)
		else:
			x = x+z5
			paths.append(2)
		if b6 <= 1:
			b6 = 4+z5
			paths.append(3)
		else:
			b6 = b6+8
			x = b6/x
			z5 = 7/b6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))