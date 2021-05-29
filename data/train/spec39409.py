import numpy as np 

def function(x):

	c6 = x
	u4 = 7
	paths = []
	try:
		if u4 >= 2:
			u4 = u4-x
			paths.append(1)
		else:
			x = 9+x
			u4 = 9+u4
			u4 = u4+3
			paths.append(2)
		if x > 2:
			x = 2/3
			u4 = x+u4
			paths.append(3)
		else:
			c6 = c6*4
			x = x*c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		u4 = c6**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))