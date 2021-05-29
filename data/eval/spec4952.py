import numpy as np 

def function(x):

	o7 = x
	c8 = x
	paths = []
	try:
		if o7 < 8:
			o7 = o7-6
			x = c8-x
			paths.append(1)
		else:
			o7 = o7*5
			c8 = c8/9
			x = o7*x
			paths.append(2)
		if x < 5:
			c8 = 0*0
			c8 = c8+3
			x = 0+x
			paths.append(3)
		else:
			o7 = 6+o7
			x = c8/2
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