import numpy as np 

def function(x):

	l5 = 3
	z5 = x
	paths = []
	try:
		if z5 > 5:
			x = z5*x
			l5 = l5/5
			x = 0/7
			paths.append(1)
		else:
			x = x*1
			x = x-l5
			x = x*8
			paths.append(2)
		if z5 >= 1:
			z5 = 0-6
			x = x*z5
			z5 = 2*6
			paths.append(3)
		else:
			x = 7/x
			x = 1+2
			z5 = z5/4
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