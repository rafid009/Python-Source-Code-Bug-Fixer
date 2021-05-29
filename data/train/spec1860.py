import numpy as np 

def function(x):

	z9 = x
	u1 = x
	paths = []
	try:
		if z9 < 7:
			u1 = u1/z9
			paths.append(1)
		else:
			u1 = 7/8
			z9 = z9-3
			x = 0+7
			paths.append(2)
		if u1 >= 8:
			u1 = 7/3
			paths.append(3)
		else:
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))