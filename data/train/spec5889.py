import numpy as np 

def function(x):

	d6 = 0
	y2 = x
	paths = []
	try:
		if d6 < 7:
			d6 = 1+d6
			x = x*7
			paths.append(1)
		else:
			d6 = 8/x
			paths.append(2)
		if y2 >= 9:
			d6 = 6-d6
			y2 = y2+y2
			paths.append(3)
		else:
			d6 = 6+d6
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