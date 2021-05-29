import numpy as np 

def function(x):

	t1 = x
	z4 = 4
	paths = []
	try:
		if t1 < 1:
			z4 = 4+2
			z4 = 1*z4
			x = x+7
			paths.append(1)
		else:
			z4 = z4*6
			paths.append(2)
		if x >= 9:
			t1 = 0+6
			paths.append(3)
		else:
			x = x/3
			x = x+2
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