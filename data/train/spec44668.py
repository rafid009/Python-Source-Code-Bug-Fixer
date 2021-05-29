import numpy as np 

def function(x):

	d8 = 0
	x3 = x
	paths = []
	try:
		if x <= 5:
			d8 = 9-d8
			x3 = x3*d8
			d8 = 8-d8
			paths.append(1)
		else:
			d8 = 0+5
			x = x/5
			paths.append(2)
		if x < 0:
			x = x*2
			d8 = d8-4
			paths.append(3)
		else:
			x3 = x3-d8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))