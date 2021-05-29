import numpy as np 

def function(x):

	a7 = 1
	d8 = 3
	paths = []
	try:
		if a7 > 6:
			a7 = d8/5
			paths.append(1)
		else:
			d8 = d8*x
			a7 = a7+7
			d8 = 7-d8
			paths.append(2)
		if d8 > 4:
			d8 = d8+3
			paths.append(3)
		else:
			a7 = a7/8
			a7 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))