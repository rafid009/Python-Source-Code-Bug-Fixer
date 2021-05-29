import numpy as np 

def function(x):

	e6 = 7
	c8 = x
	paths = []
	try:
		if e6 >= 4:
			e6 = c8-e6
			paths.append(1)
		else:
			e6 = 6-e6
			e6 = 8/x
			paths.append(2)
		if c8 <= 5:
			x = x*1
			x = x+x
			e6 = 8*c8
			paths.append(3)
		else:
			e6 = 4+e6
			e6 = e6*4
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))