import numpy as np 

def function(x):

	c0 = 4
	o2 = x
	paths = []
	try:
		if c0 > 7:
			o2 = c0/c0
			c0 = 1/c0
			paths.append(1)
		else:
			c0 = c0+9
			c0 = 5+o2
			c0 = 3+o2
			paths.append(2)
		if o2 > 3:
			o2 = c0+1
			o2 = 4-5
			paths.append(3)
		else:
			x = x/o2
			c0 = 7*c0
			o2 = o2/1
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))