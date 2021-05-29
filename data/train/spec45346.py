import numpy as np 

def function(x):

	d6 = 4
	y2 = x
	paths = []
	try:
		if x < 7:
			x = d6+x
			y2 = 0-y2
			paths.append(1)
		else:
			x = y2*3
			paths.append(2)
		if x >= 8:
			d6 = 7/y2
			paths.append(3)
		else:
			y2 = y2-2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))