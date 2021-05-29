import numpy as np 

def function(x):

	x0 = 3
	o3 = x
	paths = []
	try:
		if x < 9:
			o3 = 2+o3
			x0 = o3-7
			paths.append(1)
		else:
			x = x/5
			x = x/2
			x = x*x
			paths.append(2)
		if o3 >= 8:
			o3 = o3/o3
			paths.append(3)
		else:
			x = x/4
			o3 = 8/3
			o3 = 8+o3
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		o3 = x0**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))