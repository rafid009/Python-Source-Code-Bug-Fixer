import numpy as np 

def function(x):

	d3 = 5
	c2 = x
	paths = []
	try:
		if x <= 9:
			x = 3+x
			x = 8/x
			paths.append(1)
		else:
			c2 = x+c2
			x = x*x
			paths.append(2)
		if x < 1:
			c2 = c2-7
			x = d3-c2
			paths.append(3)
		else:
			x = c2/1
			d3 = d3+7
			d3 = d3*6
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