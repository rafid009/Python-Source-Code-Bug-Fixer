import numpy as np 

def function(x):

	q2 = 4
	z7 = x
	x = x
	paths = []
	try:
		if z7 >= 4:
			z7 = 9*2
			paths.append(1)
		else:
			z7 = q2-3
			x = z7*x
			q2 = 0-2
			paths.append(2)
		if z7 <= 1:
			x = 9+x
			x = x+x
			z7 = z7*x
			paths.append(3)
		else:
			x = x-5
			x = x/1
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