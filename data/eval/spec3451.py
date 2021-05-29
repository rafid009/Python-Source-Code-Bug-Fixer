import numpy as np 

def function(x):

	c7 = x
	d2 = 2
	paths = []
	try:
		if d2 >= 5:
			x = x/8
			x = 4/x
			c7 = 9/1
			paths.append(1)
		else:
			c7 = c7/5
			x = 1-3
			x = c7-x
			paths.append(2)
		if x <= 9:
			x = 1*x
			c7 = c7+c7
			d2 = d2-4
			paths.append(3)
		else:
			x = x-6
			d2 = 7-d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))