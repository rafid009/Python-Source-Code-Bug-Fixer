import numpy as np 

def function(x):

	n6 = x
	c5 = 2
	x = x
	paths = []
	try:
		if x > 5:
			n6 = n6*8
			n6 = 1-n6
			n6 = 8*3
			paths.append(1)
		else:
			n6 = n6-0
			c5 = n6/8
			paths.append(2)
		if n6 <= 2:
			n6 = 8/9
			n6 = n6*2
			paths.append(3)
		else:
			c5 = c5*n6
			n6 = c5-7
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))