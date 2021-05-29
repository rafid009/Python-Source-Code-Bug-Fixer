import numpy as np 

def function(x):

	c8 = x
	o3 = 4
	paths = []
	try:
		if o3 <= 1:
			x = x+x
			c8 = 5/3
			x = x+x
			paths.append(1)
		else:
			o3 = o3/o3
			o3 = c8-o3
			paths.append(2)
		if o3 > 2:
			x = 4+x
			o3 = o3/o3
			paths.append(3)
		else:
			x = c8+5
			c8 = x/c8
			x = 2+3
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		o3 = c8**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))