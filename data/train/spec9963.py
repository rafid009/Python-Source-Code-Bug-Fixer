import numpy as np 

def function(x):

	c2 = x
	u7 = 3
	x = x
	paths = []
	try:
		if x > 6:
			x = x-x
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x >= 0:
			u7 = 7+4
			u7 = u7*8
			x = 7+7
			paths.append(3)
		else:
			x = 7-1
			c2 = c2/9
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))