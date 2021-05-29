import numpy as np 

def function(x):

	z6 = x
	r7 = 3
	paths = []
	try:
		if r7 >= 3:
			r7 = r7-6
			z6 = z6*r7
			z6 = z6+7
			paths.append(1)
		else:
			r7 = 4/7
			z6 = z6/3
			z6 = 1-z6
			paths.append(2)
		if r7 >= 7:
			z6 = 8-z6
			z6 = z6-x
			paths.append(3)
		else:
			x = 5/z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))