import numpy as np 

def function(x):

	c8 = 1
	q9 = x
	paths = []
	try:
		if x <= 5:
			q9 = 0+6
			q9 = x*q9
			c8 = 6-q9
			paths.append(1)
		else:
			x = 7/5
			x = x+9
			paths.append(2)
		if c8 >= 2:
			q9 = q9*6
			x = q9+c8
			paths.append(3)
		else:
			c8 = c8*4
			q9 = 7+q9
			c8 = 4/c8
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))