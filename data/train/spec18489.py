import numpy as np 

def function(x):

	z1 = x
	r2 = 1
	paths = []
	try:
		if r2 <= 6:
			x = x*9
			r2 = r2+5
			x = 5*7
			paths.append(1)
		else:
			z1 = 5+z1
			r2 = r2-5
			z1 = r2+z1
			paths.append(2)
		if r2 > 0:
			x = 1+z1
			r2 = r2-z1
			paths.append(3)
		else:
			x = 9*5
			z1 = 5*z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		r2 = z1**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))