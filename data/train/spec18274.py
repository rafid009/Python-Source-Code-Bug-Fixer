import numpy as np 

def function(x):

	z9 = x
	d0 = x
	paths = []
	try:
		if d0 > 4:
			d0 = d0+4
			x = 7/6
			paths.append(1)
		else:
			x = 0-x
			z9 = 6-d0
			d0 = d0+1
			paths.append(2)
		if d0 > 6:
			d0 = 4/6
			x = x/6
			paths.append(3)
		else:
			d0 = 0-d0
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))