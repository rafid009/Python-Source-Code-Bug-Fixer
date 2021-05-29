import numpy as np 

def function(x):

	z5 = x
	t2 = x
	paths = []
	try:
		if z5 < 4:
			x = 2/9
			x = x*9
			z5 = z5/5
			paths.append(1)
		else:
			t2 = 1+t2
			z5 = 9/z5
			z5 = z5+5
			paths.append(2)
		if t2 > 6:
			z5 = z5+z5
			paths.append(3)
		else:
			t2 = 4*t2
			t2 = x/t2
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))