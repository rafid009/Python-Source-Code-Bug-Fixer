import numpy as np 

def function(x):

	c0 = x
	v4 = 4
	x = 8
	paths = []
	try:
		if x <= 8:
			c0 = 3*c0
			paths.append(1)
		else:
			v4 = 5-v4
			v4 = c0-7
			paths.append(2)
		if x > 4:
			x = x/1
			v4 = x-v4
			paths.append(3)
		else:
			c0 = 6+c0
			v4 = c0-v4
			c0 = c0-4
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		v4 = c0**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))