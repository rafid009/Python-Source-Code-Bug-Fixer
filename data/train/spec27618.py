import numpy as np 

def function(x):

	z5 = x
	k2 = 0
	paths = []
	try:
		if x <= 6:
			x = x/3
			k2 = k2/6
			k2 = 5+3
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if k2 >= 4:
			k2 = 7/k2
			x = 3/x
			x = x/9
			paths.append(3)
		else:
			z5 = 4+5
			x = x+2
			z5 = 9/z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))