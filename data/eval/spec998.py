import numpy as np 

def function(x):

	z1 = 3
	k6 = 4
	x = x
	paths = []
	try:
		if z1 < 5:
			k6 = 4+7
			z1 = 1/z1
			x = x-k6
			paths.append(1)
		else:
			x = x*z1
			paths.append(2)
		if x > 6:
			z1 = z1+8
			z1 = 2/7
			z1 = z1*0
			paths.append(3)
		else:
			x = x/2
			x = k6*x
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))