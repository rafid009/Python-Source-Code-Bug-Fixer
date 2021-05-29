import numpy as np 

def function(x):

	d6 = 7
	z5 = x
	paths = []
	try:
		if x >= 1:
			x = d6/2
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if d6 <= 0:
			x = x+x
			z5 = d6-7
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))