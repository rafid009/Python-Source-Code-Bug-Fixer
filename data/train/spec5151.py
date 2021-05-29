import numpy as np 

def function(x):

	j3 = 8
	c6 = 4
	paths = []
	try:
		if j3 < 9:
			x = 6-8
			j3 = 0/j3
			paths.append(1)
		else:
			j3 = j3-c6
			paths.append(2)
		if x >= 3:
			x = x-3
			paths.append(3)
		else:
			x = j3-c6
			j3 = c6*x
			j3 = x+j3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		c6 = j3**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))