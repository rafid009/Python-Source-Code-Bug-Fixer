import numpy as np 

def function(x):

	u6 = 2
	c4 = x
	paths = []
	try:
		if u6 >= 0:
			u6 = u6*u6
			u6 = 2*0
			paths.append(1)
		else:
			c4 = c4*0
			c4 = 2-7
			u6 = u6+8
			paths.append(2)
		if u6 <= 0:
			x = x-3
			x = x/x
			paths.append(3)
		else:
			c4 = 4-4
			c4 = 5/c4
			x = 9-x
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