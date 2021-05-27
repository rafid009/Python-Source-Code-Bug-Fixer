import numpy as np 

def function(x):

	o3 = 4
	c2 = x
	paths = []
	try:
		if o3 <= 9:
			o3 = 2/6
			paths.append(1)
		else:
			o3 = o3/o3
			o3 = o3-4
			o3 = o3-o3
			paths.append(2)
		if o3 < 1:
			o3 = o3/x
			paths.append(3)
		else:
			c2 = c2-x
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		o3 = c2**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))