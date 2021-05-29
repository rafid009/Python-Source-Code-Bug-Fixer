import numpy as np 

def function(x):

	d4 = 6
	y1 = 9
	paths = []
	try:
		if y1 <= 4:
			d4 = d4+5
			paths.append(1)
		else:
			x = x+4
			x = x/4
			paths.append(2)
		if y1 < 8:
			x = x*5
			y1 = y1-d4
			paths.append(3)
		else:
			y1 = y1+7
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