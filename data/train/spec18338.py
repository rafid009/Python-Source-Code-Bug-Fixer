import numpy as np 

def function(x):

	d3 = x
	o3 = x
	x = 0
	paths = []
	try:
		if d3 > 6:
			o3 = 6*o3
			x = x-d3
			paths.append(1)
		else:
			d3 = 8*4
			o3 = o3+3
			x = x-1
			paths.append(2)
		if d3 < 2:
			o3 = x+2
			paths.append(3)
		else:
			x = x-8
			x = 7+x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))