import numpy as np 

def function(x):

	z7 = 8
	t3 = 1
	paths = []
	try:
		if x >= 9:
			z7 = 1*9
			z7 = x/6
			x = x-2
			paths.append(1)
		else:
			z7 = 6*1
			t3 = 3+t3
			x = 3-x
			paths.append(2)
		if z7 < 8:
			z7 = 2+4
			paths.append(3)
		else:
			t3 = t3*4
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