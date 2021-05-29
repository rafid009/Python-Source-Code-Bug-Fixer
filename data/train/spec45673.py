import numpy as np 

def function(x):

	q5 = 0
	z9 = 9
	x = 6
	paths = []
	try:
		if z9 > 8:
			q5 = z9-4
			x = x-7
			paths.append(1)
		else:
			z9 = z9-q5
			q5 = q5/z9
			z9 = z9*q5
			paths.append(2)
		if z9 <= 0:
			q5 = z9+8
			paths.append(3)
		else:
			z9 = 9*3
			q5 = 3/q5
			q5 = q5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))