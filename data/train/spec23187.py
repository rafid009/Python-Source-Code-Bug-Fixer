import numpy as np 

def function(x):

	z9 = 7
	t7 = 1
	x = 4
	paths = []
	try:
		if t7 > 7:
			z9 = z9*z9
			x = x*x
			paths.append(1)
		else:
			z9 = 8/z9
			z9 = 1-z9
			paths.append(2)
		if z9 >= 6:
			t7 = x-x
			x = 1-9
			x = x+4
			paths.append(3)
		else:
			t7 = 2/t7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))