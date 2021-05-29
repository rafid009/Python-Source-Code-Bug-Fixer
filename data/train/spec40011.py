import numpy as np 

def function(x):

	z9 = 0
	x6 = x
	paths = []
	try:
		if x6 > 8:
			x6 = z9-x6
			paths.append(1)
		else:
			x = x+x6
			paths.append(2)
		if x6 > 6:
			z9 = z9+8
			x6 = 7+x
			paths.append(3)
		else:
			x = x*8
			z9 = z9/x
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		z9 = x6**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))