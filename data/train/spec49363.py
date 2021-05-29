import numpy as np 

def function(x):

	a1 = 6
	c4 = x
	paths = []
	try:
		if c4 <= 8:
			c4 = 9*c4
			x = c4+x
			a1 = 6-7
			paths.append(1)
		else:
			x = x+x
			a1 = 1-4
			paths.append(2)
		if c4 > 9:
			a1 = a1*c4
			a1 = 8+6
			a1 = a1*a1
			paths.append(3)
		else:
			a1 = 0/a1
			x = c4*2
			c4 = x+8
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))