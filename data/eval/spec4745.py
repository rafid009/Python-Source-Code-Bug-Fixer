import numpy as np 

def function(x):

	q2 = x
	c8 = 7
	paths = []
	try:
		if c8 >= 1:
			x = 8+x
			q2 = 6+q2
			paths.append(1)
		else:
			q2 = q2/2
			c8 = c8*7
			paths.append(2)
		if c8 < 9:
			c8 = 8*x
			x = 7*c8
			paths.append(3)
		else:
			x = q2/x
			q2 = x*9
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))