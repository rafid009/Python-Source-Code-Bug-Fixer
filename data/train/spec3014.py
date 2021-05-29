import numpy as np 

def function(x):

	c9 = x
	d6 = x
	paths = []
	try:
		if d6 <= 9:
			x = x+8
			c9 = 9/c9
			paths.append(1)
		else:
			x = 3+c9
			d6 = 3-2
			x = x+5
			paths.append(2)
		if x >= 7:
			c9 = 3*c9
			paths.append(3)
		else:
			d6 = d6-d6
			x = x*1
			x = c9*2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))