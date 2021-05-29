import numpy as np 

def function(x):

	q0 = 5
	c1 = x
	paths = []
	try:
		if q0 < 5:
			c1 = c1+q0
			q0 = q0-4
			paths.append(1)
		else:
			c1 = c1-9
			x = 1/c1
			c1 = 8-c1
			paths.append(2)
		if x < 3:
			q0 = 8+q0
			q0 = 5/q0
			paths.append(3)
		else:
			x = x+5
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		q0 = c1**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))