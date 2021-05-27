import numpy as np 

def function(x):

	o6 = x
	c3 = 1
	paths = []
	try:
		if c3 < 1:
			c3 = c3*9
			paths.append(1)
		else:
			x = o6+o6
			c3 = x*o6
			c3 = c3/o6
			paths.append(2)
		if c3 >= 1:
			c3 = 9+c3
			o6 = 0+c3
			x = x+2
			paths.append(3)
		else:
			x = x+7
			x = 7*x
			c3 = c3/1
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))