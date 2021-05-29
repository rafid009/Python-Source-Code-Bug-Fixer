import numpy as np 

def function(x):

	c5 = 6
	o2 = x
	paths = []
	try:
		if c5 >= 2:
			x = c5-x
			c5 = o2*c5
			c5 = x-c5
			paths.append(1)
		else:
			o2 = o2/5
			c5 = c5/5
			c5 = x/c5
			paths.append(2)
		if c5 <= 3:
			x = o2/2
			o2 = 5*o2
			paths.append(3)
		else:
			o2 = 3+o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))