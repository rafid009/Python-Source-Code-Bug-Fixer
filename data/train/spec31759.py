import numpy as np 

def function(x):

	o3 = 4
	a8 = 1
	paths = []
	try:
		if a8 > 5:
			o3 = 2+4
			x = 1-x
			o3 = o3+3
			paths.append(1)
		else:
			o3 = o3-1
			o3 = o3*o3
			a8 = a8/x
			paths.append(2)
		if a8 <= 6:
			x = 6*o3
			paths.append(3)
		else:
			o3 = o3*7
			a8 = a8-a8
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))