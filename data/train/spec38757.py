import numpy as np 

def function(x):

	q2 = 7
	c3 = x
	paths = []
	try:
		if x <= 6:
			c3 = c3*2
			x = 8-8
			c3 = 3+c3
			paths.append(1)
		else:
			c3 = c3-c3
			x = c3+c3
			paths.append(2)
		if x <= 3:
			q2 = 3*q2
			paths.append(3)
		else:
			q2 = 6-q2
			x = c3*8
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))