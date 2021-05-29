import numpy as np 

def function(x):

	d5 = x
	o3 = x
	paths = []
	try:
		if x <= 5:
			o3 = o3*x
			paths.append(1)
		else:
			o3 = o3/6
			o3 = o3-7
			paths.append(2)
		if d5 < 7:
			x = o3/x
			paths.append(3)
		else:
			d5 = d5-6
			d5 = 0/d5
			x = d5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))