import numpy as np 

def function(x):

	u2 = x
	c0 = x
	paths = []
	try:
		if x > 7:
			x = 0+9
			u2 = 9/u2
			x = c0-x
			paths.append(1)
		else:
			u2 = u2*5
			u2 = u2*x
			paths.append(2)
		if u2 >= 3:
			c0 = 4+c0
			c0 = c0+5
			paths.append(3)
		else:
			x = 5+1
			u2 = u2-c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))