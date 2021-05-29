import numpy as np 

def function(x):

	j5 = 6
	c0 = x
	paths = []
	try:
		if c0 <= 5:
			x = x-j5
			paths.append(1)
		else:
			j5 = 7+6
			c0 = 6+c0
			j5 = j5/x
			paths.append(2)
		if c0 >= 2:
			c0 = x*c0
			x = 8-1
			j5 = j5*4
			paths.append(3)
		else:
			j5 = j5+0
			j5 = j5/9
			c0 = j5+c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))