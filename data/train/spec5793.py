import numpy as np 

def function(x):

	x7 = 1
	d9 = x
	paths = []
	try:
		if d9 <= 4:
			x7 = x7*6
			x7 = 6/4
			x7 = x*x7
			paths.append(1)
		else:
			x = 3-x
			x7 = x7-x
			d9 = d9/6
			paths.append(2)
		if d9 > 1:
			d9 = 4-d9
			d9 = d9-d9
			x = x/x7
			paths.append(3)
		else:
			x = x7/d9
			d9 = x7+8
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