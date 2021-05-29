import numpy as np 

def function(x):

	y6 = 6
	d1 = 3
	paths = []
	try:
		if x <= 4:
			d1 = x-d1
			x = 6/d1
			y6 = d1*y6
			paths.append(1)
		else:
			x = x+4
			d1 = d1+2
			y6 = y6/7
			paths.append(2)
		if d1 < 6:
			x = d1-x
			x = x-6
			paths.append(3)
		else:
			d1 = x+d1
			x = x/9
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