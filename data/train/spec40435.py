import numpy as np 

def function(x):

	d7 = 3
	c1 = x
	x = 1
	paths = []
	try:
		if d7 > 4:
			c1 = 9-c1
			x = 5/x
			c1 = c1-d7
			paths.append(1)
		else:
			c1 = 9*c1
			d7 = c1-9
			paths.append(2)
		if d7 >= 6:
			x = 8-x
			c1 = c1*6
			d7 = c1+7
			paths.append(3)
		else:
			d7 = 2+x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))