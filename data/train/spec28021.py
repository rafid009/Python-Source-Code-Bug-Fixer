import numpy as np 

def function(x):

	z5 = x
	t4 = x
	paths = []
	try:
		if x > 2:
			z5 = z5-z5
			x = x*z5
			paths.append(1)
		else:
			z5 = 1/2
			paths.append(2)
		if z5 <= 4:
			z5 = 3*7
			paths.append(3)
		else:
			z5 = x+2
			x = 5+2
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))