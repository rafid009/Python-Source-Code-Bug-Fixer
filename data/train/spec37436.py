import numpy as np 

def function(x):

	d1 = 1
	c6 = x
	paths = []
	try:
		if d1 >= 0:
			c6 = c6+d1
			x = 3*x
			c6 = d1*9
			paths.append(1)
		else:
			c6 = 9*7
			d1 = d1-c6
			c6 = x+4
			paths.append(2)
		if x <= 9:
			d1 = d1+3
			c6 = x-c6
			paths.append(3)
		else:
			d1 = d1-d1
			d1 = d1-c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		d1 = c6**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))