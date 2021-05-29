import numpy as np 

def function(x):

	y1 = 1
	d5 = x
	x = 4
	paths = []
	try:
		if x > 7:
			y1 = y1/4
			d5 = d5-d5
			paths.append(1)
		else:
			x = x-3
			x = d5-y1
			x = 3-x
			paths.append(2)
		if d5 >= 4:
			d5 = 3+4
			x = 8+x
			x = 4+5
			paths.append(3)
		else:
			x = x+1
			d5 = d5/y1
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))