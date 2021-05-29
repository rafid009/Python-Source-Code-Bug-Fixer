import numpy as np 

def function(x):

	o3 = x
	c2 = 0
	x = 4
	paths = []
	try:
		if x < 8:
			c2 = 6-x
			paths.append(1)
		else:
			c2 = 0/c2
			paths.append(2)
		if x <= 5:
			c2 = 8-c2
			c2 = o3-7
			paths.append(3)
		else:
			x = 9-5
			o3 = o3*6
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))