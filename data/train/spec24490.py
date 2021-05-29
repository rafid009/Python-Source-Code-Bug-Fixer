import numpy as np 

def function(x):

	t2 = 1
	z6 = x
	paths = []
	try:
		if z6 < 6:
			x = x-0
			x = 7+6
			paths.append(1)
		else:
			x = x+0
			t2 = t2+5
			z6 = 2+5
			paths.append(2)
		if z6 < 2:
			x = x*2
			z6 = 6*t2
			paths.append(3)
		else:
			z6 = 6-z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))