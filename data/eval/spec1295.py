import numpy as np 

def function(x):

	c4 = x
	n3 = 5
	paths = []
	try:
		if c4 > 7:
			c4 = c4*5
			x = 3+x
			c4 = c4/3
			paths.append(1)
		else:
			c4 = c4+5
			x = 2-9
			c4 = x*1
			paths.append(2)
		if x >= 5:
			x = x-x
			c4 = c4/6
			paths.append(3)
		else:
			x = 4*0
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