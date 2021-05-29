import numpy as np 

def function(x):

	j5 = x
	o3 = x
	paths = []
	try:
		if j5 <= 9:
			o3 = o3/7
			paths.append(1)
		else:
			j5 = 5-o3
			paths.append(2)
		if o3 < 2:
			j5 = j5+7
			j5 = 2/j5
			paths.append(3)
		else:
			o3 = o3-o3
			o3 = o3-6
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