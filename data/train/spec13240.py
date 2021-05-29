import numpy as np 

def function(x):

	o3 = x
	u9 = 4
	paths = []
	try:
		if x >= 9:
			x = o3-u9
			paths.append(1)
		else:
			x = x+4
			x = x-3
			o3 = o3-3
			paths.append(2)
		if o3 <= 4:
			x = 6-2
			o3 = o3/x
			paths.append(3)
		else:
			o3 = 1-o3
			o3 = u9*o3
			o3 = o3/3
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		u9 = o3**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))