import numpy as np 

def function(x):

	o8 = x
	d3 = 8
	paths = []
	try:
		if d3 < 9:
			x = d3+x
			paths.append(1)
		else:
			o8 = o8+7
			paths.append(2)
		if d3 <= 1:
			o8 = o8*o8
			x = o8*x
			x = 3-x
			paths.append(3)
		else:
			o8 = 0-x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))