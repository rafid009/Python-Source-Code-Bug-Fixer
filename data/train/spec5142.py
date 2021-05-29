import numpy as np 

def function(x):

	c6 = x
	u4 = x
	paths = []
	try:
		if u4 >= 5:
			c6 = c6*c6
			c6 = 1*c6
			paths.append(1)
		else:
			c6 = c6/5
			u4 = u4+c6
			u4 = u4+c6
			paths.append(2)
		if x < 2:
			u4 = u4/9
			x = 5+x
			paths.append(3)
		else:
			x = 8*u4
			x = x+2
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))