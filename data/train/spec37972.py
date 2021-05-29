import numpy as np 

def function(x):

	o3 = x
	u2 = x
	paths = []
	try:
		if x > 2:
			o3 = o3-o3
			x = 5+o3
			o3 = 2+u2
			paths.append(1)
		else:
			x = x/4
			u2 = 0-x
			paths.append(2)
		if o3 > 7:
			o3 = o3/7
			x = 9+8
			paths.append(3)
		else:
			x = u2/x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))