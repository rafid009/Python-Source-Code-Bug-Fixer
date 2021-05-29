import numpy as np 

def function(x):

	c7 = x
	o7 = x
	paths = []
	try:
		if o7 > 9:
			c7 = x-3
			o7 = o7*c7
			x = 0/4
			paths.append(1)
		else:
			x = 2/x
			x = 0+x
			c7 = x*c7
			paths.append(2)
		if o7 > 5:
			x = o7*5
			x = x/o7
			o7 = x-5
			paths.append(3)
		else:
			o7 = o7-x
			o7 = o7+2
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o7 = o7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))