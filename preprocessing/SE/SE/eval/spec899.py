import numpy as np 

def function(x):

	c8 = 4
	j7 = 9
	paths = []
	try:
		if j7 < 8:
			j7 = j7+9
			j7 = j7+5
			paths.append(1)
		else:
			j7 = j7+6
			paths.append(2)
		if x > 6:
			c8 = c8-7
			c8 = c8-9
			paths.append(3)
		else:
			j7 = j7-3
			j7 = j7/4
			c8 = 7-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))