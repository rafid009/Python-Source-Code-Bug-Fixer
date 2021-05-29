import numpy as np 

def function(x):

	z5 = x
	q5 = x
	x = x
	paths = []
	try:
		if x < 7:
			q5 = x-9
			x = 9/x
			paths.append(1)
		else:
			z5 = z5/2
			paths.append(2)
		if z5 >= 1:
			x = x*5
			x = 6+9
			q5 = q5*x
			paths.append(3)
		else:
			z5 = 5*z5
			x = x+2
			x = z5-x
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