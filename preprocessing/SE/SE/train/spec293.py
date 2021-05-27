import numpy as np 

def function(x):

	z5 = 1
	u9 = x
	paths = []
	try:
		if x >= 6:
			u9 = u9/9
			z5 = z5*8
			paths.append(1)
		else:
			x = 7+x
			x = u9/x
			paths.append(2)
		if u9 <= 2:
			u9 = u9*u9
			z5 = z5-5
			paths.append(3)
		else:
			x = x-8
			z5 = z5/2
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))