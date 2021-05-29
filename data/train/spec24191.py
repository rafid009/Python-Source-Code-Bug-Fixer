import numpy as np 

def function(x):

	c6 = 4
	d7 = x
	paths = []
	try:
		if x < 9:
			c6 = 7*d7
			x = x+x
			x = x+8
			paths.append(1)
		else:
			d7 = 4-d7
			x = x-9
			c6 = 3+c6
			paths.append(2)
		if d7 > 6:
			d7 = 8-d7
			c6 = 0-9
			x = x*4
			paths.append(3)
		else:
			d7 = d7-4
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))