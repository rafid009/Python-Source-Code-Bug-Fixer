import numpy as np 

def function(x):

	d5 = x
	z4 = x
	paths = []
	try:
		if x < 4:
			z4 = d5/5
			d5 = 2*z4
			x = d5+9
			paths.append(1)
		else:
			d5 = d5*5
			x = x+3
			x = 2-1
			paths.append(2)
		if x > 5:
			z4 = z4*d5
			d5 = d5-1
			z4 = 9+7
			paths.append(3)
		else:
			x = x+d5
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))