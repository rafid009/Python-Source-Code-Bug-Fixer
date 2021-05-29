import numpy as np 

def function(x):

	z5 = x
	r8 = 0
	paths = []
	try:
		if z5 > 7:
			z5 = 5-z5
			x = x+0
			r8 = z5*1
			paths.append(1)
		else:
			x = x-9
			r8 = 0-r8
			r8 = 9*r8
			paths.append(2)
		if x <= 9:
			r8 = 2/7
			z5 = z5*z5
			x = x/z5
			paths.append(3)
		else:
			r8 = r8/z5
			x = 5/x
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