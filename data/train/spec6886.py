import numpy as np 

def function(x):

	o3 = 1
	x6 = x
	paths = []
	try:
		if x6 >= 8:
			x6 = x+7
			o3 = o3+o3
			x6 = x6+7
			paths.append(1)
		else:
			x = 5*x
			o3 = 9*o3
			paths.append(2)
		if x <= 5:
			x = 9/x
			x6 = 6+7
			x = x-6
			paths.append(3)
		else:
			x = 9-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))