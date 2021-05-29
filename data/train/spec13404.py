import numpy as np 

def function(x):

	q8 = 7
	c5 = x
	paths = []
	try:
		if x > 2:
			x = 0-x
			paths.append(1)
		else:
			c5 = 9+c5
			paths.append(2)
		if c5 >= 5:
			x = x/1
			c5 = q8*1
			paths.append(3)
		else:
			q8 = q8+c5
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))