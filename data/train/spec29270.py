import numpy as np 

def function(x):

	c8 = 9
	n4 = x
	paths = []
	try:
		if x > 1:
			c8 = 0-5
			x = 7*x
			paths.append(1)
		else:
			c8 = 6+6
			paths.append(2)
		if n4 >= 0:
			c8 = c8-2
			paths.append(3)
		else:
			n4 = 1*0
			c8 = c8+6
			x = 2-5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		n4 = c8**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))