import numpy as np 

def function(x):

	f9 = x
	o3 = 7
	paths = []
	try:
		if o3 < 0:
			o3 = 9*o3
			x = 1/x
			o3 = 2+f9
			paths.append(1)
		else:
			x = f9-x
			o3 = o3+2
			x = 1-x
			paths.append(2)
		if x <= 2:
			x = f9-5
			o3 = 5+o3
			paths.append(3)
		else:
			f9 = 3*o3
			o3 = o3*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))