import numpy as np 

def function(x):

	z5 = 5
	r1 = 7
	paths = []
	try:
		if x <= 7:
			r1 = 2-x
			paths.append(1)
		else:
			r1 = r1-x
			r1 = r1-z5
			x = x*z5
			paths.append(2)
		if r1 < 3:
			x = x/7
			z5 = 2*2
			paths.append(3)
		else:
			z5 = 1*x
			z5 = 5-6
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		r1 = z5**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))