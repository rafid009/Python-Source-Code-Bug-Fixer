import numpy as np 

def function(x):

	g9 = 3
	d7 = 1
	paths = []
	try:
		if g9 > 3:
			g9 = 7-g9
			d7 = d7-6
			x = 5-x
			paths.append(1)
		else:
			x = x-8
			d7 = 3/d7
			d7 = 3+d7
			paths.append(2)
		if x > 5:
			x = 3/8
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))