import numpy as np 

def function(x):

	d9 = x
	o3 = 6
	paths = []
	try:
		if x > 7:
			d9 = o3+d9
			paths.append(1)
		else:
			o3 = d9-2
			x = x/x
			o3 = o3-x
			paths.append(2)
		if d9 < 8:
			x = d9+7
			paths.append(3)
		else:
			x = x-x
			o3 = o3-x
			o3 = d9-2
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