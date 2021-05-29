import numpy as np 

def function(x):

	o5 = x
	c3 = 8
	paths = []
	try:
		if o5 > 1:
			o5 = 7*o5
			c3 = 7-c3
			paths.append(1)
		else:
			c3 = c3*c3
			paths.append(2)
		if x >= 3:
			o5 = o5+8
			paths.append(3)
		else:
			c3 = x+5
			x = c3+1
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