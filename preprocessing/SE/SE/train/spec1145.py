import numpy as np 

def function(x):

	c5 = 6
	q9 = x
	paths = []
	try:
		if q9 <= 9:
			q9 = 1*q9
			q9 = q9-5
			paths.append(1)
		else:
			c5 = c5+x
			x = x/x
			paths.append(2)
		if c5 >= 7:
			x = 8*1
			paths.append(3)
		else:
			q9 = 6+1
			c5 = c5/5
			c5 = q9/c5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))