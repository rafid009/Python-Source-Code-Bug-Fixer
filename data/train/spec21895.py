import numpy as np 

def function(x):

	d7 = 2
	x7 = x
	paths = []
	try:
		if x <= 4:
			d7 = 6/d7
			paths.append(1)
		else:
			d7 = d7*d7
			d7 = x*d7
			x = x/x7
			paths.append(2)
		if x7 >= 4:
			d7 = 1/5
			x7 = x7/7
			d7 = 5+d7
			paths.append(3)
		else:
			d7 = 8-4
			d7 = 8*x
			x7 = x7*2
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