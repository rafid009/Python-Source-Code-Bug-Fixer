import numpy as np 

def function(x):

	f4 = x
	c2 = x
	paths = []
	try:
		if f4 > 7:
			f4 = 1*5
			c2 = 7+c2
			x = x/x
			paths.append(1)
		else:
			c2 = c2-0
			f4 = 3/f4
			paths.append(2)
		if x < 7:
			x = 4-x
			x = 4*1
			c2 = c2*x
			paths.append(3)
		else:
			x = 3-x
			x = 6+x
			c2 = c2/x
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