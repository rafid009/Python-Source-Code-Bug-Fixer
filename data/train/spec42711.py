import numpy as np 

def function(x):

	z1 = x
	x2 = x
	paths = []
	try:
		if x2 < 1:
			x2 = x+5
			x2 = x2/9
			paths.append(1)
		else:
			z1 = z1/z1
			paths.append(2)
		if x2 < 1:
			z1 = z1*7
			x2 = 4/x
			x2 = 3/x2
			paths.append(3)
		else:
			z1 = x2*z1
			x = x*2
			x2 = x2-z1
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))