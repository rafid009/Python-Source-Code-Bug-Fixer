import numpy as np 

def function(x):

	z1 = 3
	r6 = x
	x = 8
	paths = []
	try:
		if r6 <= 1:
			z1 = z1/z1
			z1 = r6*z1
			paths.append(1)
		else:
			r6 = z1-x
			x = x/9
			paths.append(2)
		if x > 8:
			r6 = r6/9
			x = 2-x
			z1 = 5-3
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))