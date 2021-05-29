import numpy as np 

def function(x):

	z6 = x
	r8 = 6
	x = 7
	paths = []
	try:
		if r8 >= 3:
			x = x-8
			paths.append(1)
		else:
			x = 5*x
			z6 = 9*4
			paths.append(2)
		if r8 > 6:
			r8 = r8/5
			z6 = 1/z6
			z6 = z6*5
			paths.append(3)
		else:
			r8 = 5-r8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))