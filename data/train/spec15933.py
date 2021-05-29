import numpy as np 

def function(x):

	i1 = 0
	z5 = 0
	paths = []
	try:
		if i1 <= 1:
			z5 = z5-x
			paths.append(1)
		else:
			z5 = 3*z5
			paths.append(2)
		if x > 7:
			z5 = x+7
			x = x*7
			i1 = i1/5
			paths.append(3)
		else:
			z5 = z5+0
			z5 = 4-6
			i1 = 3+x
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