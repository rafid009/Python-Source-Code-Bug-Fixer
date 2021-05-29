import numpy as np 

def function(x):

	z4 = 8
	t5 = x
	paths = []
	try:
		if z4 > 0:
			z4 = z4*3
			t5 = t5-8
			z4 = z4+0
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if z4 <= 4:
			t5 = x/t5
			paths.append(3)
		else:
			x = x-z4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))