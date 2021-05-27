import numpy as np 

def function(x):

	f7 = x
	c4 = x
	paths = []
	try:
		if x < 8:
			f7 = 8+f7
			c4 = c4/f7
			paths.append(1)
		else:
			f7 = 1+f7
			f7 = 8/3
			paths.append(2)
		if c4 > 7:
			x = x/6
			paths.append(3)
		else:
			x = x*5
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