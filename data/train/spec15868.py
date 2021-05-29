import numpy as np 

def function(x):

	r9 = x
	z1 = 8
	paths = []
	try:
		if r9 >= 6:
			r9 = r9/9
			x = r9*4
			paths.append(1)
		else:
			z1 = x-3
			paths.append(2)
		if r9 > 6:
			x = 9*5
			r9 = r9+4
			z1 = 6+1
			paths.append(3)
		else:
			r9 = 0+r9
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))