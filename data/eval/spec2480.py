import numpy as np 

def function(x):

	y7 = x
	d4 = x
	x = 3
	paths = []
	try:
		if x <= 6:
			y7 = 6+y7
			paths.append(1)
		else:
			y7 = 0/6
			y7 = y7-7
			y7 = 1+y7
			paths.append(2)
		if y7 <= 3:
			d4 = x+y7
			x = 4*d4
			x = x+d4
			paths.append(3)
		else:
			x = x*x
			d4 = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))