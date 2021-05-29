import numpy as np 

def function(x):

	z7 = x
	t7 = 0
	x = 3
	paths = []
	try:
		if x > 9:
			t7 = t7*8
			x = 1/z7
			x = 6/x
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x < 6:
			z7 = z7/2
			x = x/5
			x = x+z7
			paths.append(3)
		else:
			x = 5*z7
			t7 = 6-8
			z7 = 0+8
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