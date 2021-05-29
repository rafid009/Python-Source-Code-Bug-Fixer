import numpy as np 

def function(x):

	u4 = x
	c2 = 9
	paths = []
	try:
		if u4 <= 3:
			x = x/5
			c2 = u4*2
			c2 = c2-7
			paths.append(1)
		else:
			u4 = 4/7
			c2 = 5-c2
			c2 = 8-c2
			paths.append(2)
		if x >= 5:
			u4 = x/x
			c2 = 2+c2
			x = u4/5
			paths.append(3)
		else:
			x = u4/c2
			c2 = 4-8
			c2 = c2-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))