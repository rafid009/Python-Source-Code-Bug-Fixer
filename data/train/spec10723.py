import numpy as np 

def function(x):

	t4 = 6
	z8 = x
	paths = []
	try:
		if z8 >= 1:
			t4 = t4-3
			t4 = t4/4
			paths.append(1)
		else:
			z8 = z8*0
			paths.append(2)
		if z8 >= 4:
			t4 = t4+1
			z8 = t4+6
			t4 = t4+3
			paths.append(3)
		else:
			x = 1/x
			z8 = 6*2
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))