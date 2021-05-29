import numpy as np 

def function(x):

	q0 = 6
	c2 = 9
	paths = []
	try:
		if x >= 1:
			c2 = c2*c2
			paths.append(1)
		else:
			x = 3-x
			q0 = 5-q0
			paths.append(2)
		if x >= 4:
			c2 = c2+9
			c2 = q0*9
			paths.append(3)
		else:
			x = x*9
			c2 = 0*c2
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))