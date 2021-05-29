import numpy as np 

def function(x):

	v8 = 0
	o3 = 9
	paths = []
	try:
		if x >= 9:
			x = 4*6
			v8 = o3-v8
			paths.append(1)
		else:
			o3 = o3*1
			o3 = x+o3
			paths.append(2)
		if o3 > 4:
			o3 = v8-o3
			paths.append(3)
		else:
			v8 = v8+6
			o3 = 6-5
			v8 = 3+v8
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