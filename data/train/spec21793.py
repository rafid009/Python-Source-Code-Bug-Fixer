import numpy as np 

def function(x):

	c8 = 9
	l2 = 9
	paths = []
	try:
		if x <= 8:
			c8 = c8/x
			paths.append(1)
		else:
			l2 = l2-4
			l2 = 8+l2
			x = l2+9
			paths.append(2)
		if x > 7:
			x = x-7
			l2 = 9*l2
			l2 = x*l2
			paths.append(3)
		else:
			x = x/2
			x = x/8
			x = 8*l2
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))