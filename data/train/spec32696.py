import numpy as np 

def function(x):

	r9 = x
	z6 = x
	paths = []
	try:
		if z6 >= 8:
			r9 = 1/z6
			paths.append(1)
		else:
			z6 = r9/3
			paths.append(2)
		if r9 > 0:
			z6 = z6+7
			x = x/z6
			paths.append(3)
		else:
			z6 = r9/z6
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))