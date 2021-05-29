import numpy as np 

def function(x):

	d3 = 8
	c2 = x
	paths = []
	try:
		if x < 9:
			d3 = 1+9
			c2 = 7/c2
			paths.append(1)
		else:
			d3 = 1+d3
			x = x*3
			paths.append(2)
		if x <= 7:
			d3 = d3+x
			d3 = x+x
			paths.append(3)
		else:
			d3 = d3/5
			c2 = d3-c2
			d3 = c2-d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d3 = d3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))