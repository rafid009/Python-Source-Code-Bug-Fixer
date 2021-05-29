import numpy as np 

def function(x):

	d9 = x
	d6 = 2
	paths = []
	try:
		if x >= 0:
			x = 9*x
			d9 = 6-d9
			paths.append(1)
		else:
			d9 = x/7
			d9 = 1+d9
			paths.append(2)
		if x > 0:
			x = x*d6
			d6 = d6-d6
			paths.append(3)
		else:
			d6 = d9*d6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))