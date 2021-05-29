import numpy as np 

def function(x):

	w8 = 5
	o3 = 7
	paths = []
	try:
		if w8 < 2:
			x = x-o3
			paths.append(1)
		else:
			o3 = w8*o3
			paths.append(2)
		if x <= 0:
			x = 2*x
			paths.append(3)
		else:
			o3 = 9/8
			o3 = o3-7
			x = 2-2
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