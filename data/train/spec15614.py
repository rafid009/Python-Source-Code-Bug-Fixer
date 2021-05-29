import numpy as np 

def function(x):

	d8 = x
	x7 = x
	x = 4
	paths = []
	try:
		if d8 <= 4:
			d8 = d8+x
			x7 = x7/6
			paths.append(1)
		else:
			x7 = d8+6
			x = x/x
			d8 = d8-x
			paths.append(2)
		if x <= 1:
			x7 = d8*x7
			x = x*x7
			x7 = 7-1
			paths.append(3)
		else:
			d8 = 5/7
			x = 7/x
			d8 = d8+7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		d8 = x7**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))