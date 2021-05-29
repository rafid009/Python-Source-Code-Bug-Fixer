import numpy as np 

def function(x):

	p9 = 1
	z5 = 6
	paths = []
	try:
		if p9 <= 6:
			z5 = z5/9
			x = 1-2
			z5 = z5+x
			paths.append(1)
		else:
			x = 2/8
			z5 = 2/6
			paths.append(2)
		if p9 >= 8:
			x = p9/5
			z5 = z5/5
			paths.append(3)
		else:
			x = p9-x
			p9 = z5+p9
			x = 7-x
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