import numpy as np 

def function(x):

	o3 = x
	v4 = x
	paths = []
	try:
		if v4 >= 6:
			x = x+v4
			v4 = 1-v4
			paths.append(1)
		else:
			v4 = v4*o3
			o3 = v4+o3
			paths.append(2)
		if x > 9:
			v4 = v4/1
			paths.append(3)
		else:
			v4 = 8/v4
			x = x+o3
			x = x/8
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