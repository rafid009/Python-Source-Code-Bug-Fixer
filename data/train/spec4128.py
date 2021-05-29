import numpy as np 

def function(x):

	z6 = 3
	q9 = x
	paths = []
	try:
		if z6 < 4:
			x = 3+x
			z6 = x+x
			z6 = 9*z6
			paths.append(1)
		else:
			x = x-2
			x = 4/q9
			paths.append(2)
		if x >= 8:
			z6 = 6-z6
			q9 = 9/z6
			paths.append(3)
		else:
			q9 = 6/7
			q9 = q9/3
			x = z6+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))