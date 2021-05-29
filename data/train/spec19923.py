import numpy as np 

def function(x):

	d9 = x
	z9 = 9
	x = x
	paths = []
	try:
		if x <= 6:
			z9 = 4*z9
			x = 3/x
			z9 = d9*7
			paths.append(1)
		else:
			x = x/7
			z9 = 5+d9
			paths.append(2)
		if z9 >= 5:
			d9 = d9/d9
			paths.append(3)
		else:
			x = x-5
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))