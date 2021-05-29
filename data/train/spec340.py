import numpy as np 

def function(x):

	o2 = x
	c8 = x
	paths = []
	try:
		if o2 <= 6:
			o2 = o2-9
			c8 = c8+x
			paths.append(1)
		else:
			x = o2/7
			o2 = o2+1
			paths.append(2)
		if x < 4:
			o2 = o2/o2
			o2 = o2/x
			paths.append(3)
		else:
			c8 = c8-x
			c8 = o2-5
			o2 = o2/4
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		c8 = o2**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))