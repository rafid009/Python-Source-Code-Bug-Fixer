import numpy as np 

def function(x):

	c5 = 9
	q4 = 2
	paths = []
	try:
		if c5 <= 3:
			q4 = q4*6
			c5 = c5-3
			x = 9+7
			paths.append(1)
		else:
			x = x*q4
			c5 = 5-c5
			q4 = q4*1
			paths.append(2)
		if q4 >= 5:
			x = c5/4
			x = x+x
			paths.append(3)
		else:
			q4 = q4+q4
			q4 = 4/c5
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))