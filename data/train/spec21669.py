import numpy as np 

def function(x):

	o9 = x
	c6 = 1
	paths = []
	try:
		if x < 6:
			o9 = o9+c6
			o9 = o9/3
			paths.append(1)
		else:
			c6 = o9+4
			o9 = o9-0
			x = 9+1
			paths.append(2)
		if x < 3:
			o9 = o9/6
			c6 = c6/1
			paths.append(3)
		else:
			o9 = x-o9
			o9 = o9-x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))