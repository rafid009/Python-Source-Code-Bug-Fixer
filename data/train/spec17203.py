import numpy as np 

def function(x):

	z6 = x
	a4 = x
	paths = []
	try:
		if x < 8:
			x = x*5
			z6 = z6-4
			paths.append(1)
		else:
			x = x-2
			x = x+1
			x = x-z6
			paths.append(2)
		if z6 <= 3:
			a4 = 9+3
			x = x/5
			paths.append(3)
		else:
			z6 = 4*x
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