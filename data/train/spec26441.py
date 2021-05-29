import numpy as np 

def function(x):

	q6 = 7
	c5 = x
	paths = []
	try:
		if x >= 3:
			x = q6+0
			paths.append(1)
		else:
			q6 = q6-c5
			paths.append(2)
		if x <= 6:
			x = x*8
			c5 = c5/5
			x = x*1
			paths.append(3)
		else:
			q6 = 2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))