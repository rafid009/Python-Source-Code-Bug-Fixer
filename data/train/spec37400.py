import numpy as np 

def function(x):

	r8 = x
	c8 = 6
	paths = []
	try:
		if r8 >= 5:
			c8 = 5*c8
			x = x+x
			x = x/6
			paths.append(1)
		else:
			x = 9-x
			c8 = c8+x
			paths.append(2)
		if r8 > 2:
			r8 = r8/8
			paths.append(3)
		else:
			c8 = r8-x
			x = 4-c8
			x = x-0
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))