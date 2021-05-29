import numpy as np 

def function(x):

	n7 = 7
	c8 = 4
	paths = []
	try:
		if n7 > 8:
			c8 = n7-0
			paths.append(1)
		else:
			x = x-6
			c8 = c8-c8
			paths.append(2)
		if n7 >= 2:
			n7 = 5/x
			n7 = n7/5
			c8 = x-n7
			paths.append(3)
		else:
			x = c8+3
			x = x+8
			x = 5+8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		n7 = c8**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))