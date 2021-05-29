import numpy as np 

def function(x):

	c0 = x
	k4 = 5
	paths = []
	try:
		if c0 <= 3:
			k4 = k4+k4
			c0 = x*1
			k4 = x*2
			paths.append(1)
		else:
			x = x*2
			x = 4*x
			paths.append(2)
		if c0 > 7:
			c0 = c0/3
			paths.append(3)
		else:
			k4 = k4-c0
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))