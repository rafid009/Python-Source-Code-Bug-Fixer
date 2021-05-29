import numpy as np 

def function(x):

	c5 = 0
	q4 = 6
	paths = []
	try:
		if q4 >= 8:
			q4 = q4/c5
			x = 2+x
			c5 = 0+3
			paths.append(1)
		else:
			q4 = x*8
			q4 = q4-0
			paths.append(2)
		if x < 2:
			c5 = x-q4
			c5 = q4*9
			paths.append(3)
		else:
			x = 5-q4
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))