import numpy as np 

def function(x):

	d3 = 3
	c2 = x
	paths = []
	try:
		if c2 > 0:
			x = d3+d3
			x = 5*3
			c2 = d3+c2
			paths.append(1)
		else:
			d3 = d3-8
			d3 = c2/1
			paths.append(2)
		if x > 7:
			x = x/x
			d3 = 1*x
			x = x-c2
			paths.append(3)
		else:
			c2 = c2-0
			c2 = 5/d3
			d3 = 1+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))