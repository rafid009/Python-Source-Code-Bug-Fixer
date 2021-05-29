import numpy as np 

def function(x):

	o3 = x
	d6 = 5
	paths = []
	try:
		if d6 <= 4:
			o3 = o3-d6
			paths.append(1)
		else:
			o3 = 9*o3
			paths.append(2)
		if x > 6:
			o3 = 7/d6
			d6 = d6/d6
			paths.append(3)
		else:
			o3 = o3-4
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		x = o3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))