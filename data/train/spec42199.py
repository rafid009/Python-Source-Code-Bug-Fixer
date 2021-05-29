import numpy as np 

def function(x):

	z8 = 7
	t1 = x
	paths = []
	try:
		if t1 < 8:
			z8 = z8/1
			z8 = 6/8
			paths.append(1)
		else:
			x = 9+z8
			z8 = z8*z8
			paths.append(2)
		if z8 >= 5:
			x = x-x
			paths.append(3)
		else:
			z8 = 8-z8
			t1 = 4-6
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))