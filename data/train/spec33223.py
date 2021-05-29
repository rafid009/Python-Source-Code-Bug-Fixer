import numpy as np 

def function(x):

	o3 = 1
	d6 = x
	paths = []
	try:
		if x > 4:
			d6 = x+2
			o3 = o3/x
			paths.append(1)
		else:
			d6 = d6/6
			x = x/2
			paths.append(2)
		if d6 <= 3:
			o3 = 7-7
			x = x+5
			o3 = o3+o3
			paths.append(3)
		else:
			x = x-1
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