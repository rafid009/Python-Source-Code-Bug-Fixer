import numpy as np 

def function(x):

	b1 = x
	o3 = 5
	paths = []
	try:
		if x >= 8:
			x = o3-7
			b1 = 9+6
			x = 4-x
			paths.append(1)
		else:
			x = x-7
			b1 = 8*x
			x = x/o3
			paths.append(2)
		if o3 < 3:
			x = x+o3
			x = x-o3
			x = 4/x
			paths.append(3)
		else:
			o3 = o3+o3
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))