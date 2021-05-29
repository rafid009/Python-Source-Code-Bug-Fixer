import numpy as np 

def function(x):

	y0 = 8
	d9 = 1
	paths = []
	try:
		if y0 <= 7:
			d9 = 5*7
			paths.append(1)
		else:
			y0 = 1-y0
			d9 = x+3
			paths.append(2)
		if d9 <= 5:
			x = x+3
			paths.append(3)
		else:
			d9 = y0+3
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))