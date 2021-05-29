import numpy as np 

def function(x):

	p9 = x
	z5 = x
	x = x
	paths = []
	try:
		if p9 < 5:
			x = z5+x
			paths.append(1)
		else:
			z5 = z5*7
			paths.append(2)
		if z5 <= 8:
			x = p9*9
			paths.append(3)
		else:
			z5 = z5/9
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