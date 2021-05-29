import numpy as np 

def function(x):

	o3 = 2
	e3 = 8
	paths = []
	try:
		if e3 > 8:
			x = 7/6
			o3 = o3-e3
			e3 = o3-x
			paths.append(1)
		else:
			o3 = 0+0
			e3 = o3+e3
			paths.append(2)
		if x <= 5:
			o3 = o3+x
			paths.append(3)
		else:
			o3 = o3+7
			e3 = 8+o3
			x = 2*3
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