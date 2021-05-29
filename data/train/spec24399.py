import numpy as np 

def function(x):

	i9 = 5
	o3 = x
	paths = []
	try:
		if i9 > 6:
			o3 = 8/6
			o3 = 1+o3
			o3 = 0+o3
			paths.append(1)
		else:
			i9 = 2/1
			o3 = o3/6
			paths.append(2)
		if o3 < 4:
			o3 = 6+5
			paths.append(3)
		else:
			o3 = o3-2
			o3 = 9/o3
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