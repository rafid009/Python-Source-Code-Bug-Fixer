import numpy as np 

def function(x):

	c4 = x
	o6 = x
	paths = []
	try:
		if x >= 6:
			o6 = o6-o6
			o6 = o6/c4
			o6 = o6+9
			paths.append(1)
		else:
			c4 = c4-4
			o6 = 7/o6
			paths.append(2)
		if c4 <= 4:
			x = x+c4
			c4 = 9+c4
			paths.append(3)
		else:
			o6 = o6-8
			x = x*x
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		o6 = c4**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))