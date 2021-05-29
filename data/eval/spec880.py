import numpy as np 

def function(x):

	c4 = 6
	n5 = 9
	paths = []
	try:
		if x > 4:
			x = x-n5
			c4 = c4-x
			paths.append(1)
		else:
			c4 = c4/n5
			paths.append(2)
		if x <= 3:
			c4 = 2+c4
			paths.append(3)
		else:
			n5 = 3*x
			x = n5*c4
			x = x*1
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