import numpy as np 

def function(x):

	c2 = 5
	q0 = x
	paths = []
	try:
		if q0 <= 2:
			c2 = c2/3
			x = 4-2
			c2 = c2/9
			paths.append(1)
		else:
			q0 = 2*4
			paths.append(2)
		if x > 9:
			x = x/6
			x = x+q0
			paths.append(3)
		else:
			c2 = x-c2
			c2 = c2/9
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))