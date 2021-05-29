import numpy as np 

def function(x):

	y2 = 4
	d6 = x
	paths = []
	try:
		if d6 > 1:
			y2 = d6*y2
			y2 = 1-d6
			d6 = 2*d6
			paths.append(1)
		else:
			d6 = x+5
			x = d6*x
			paths.append(2)
		if y2 >= 8:
			d6 = d6-y2
			x = x/7
			paths.append(3)
		else:
			d6 = y2/5
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		d6 = y2**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))