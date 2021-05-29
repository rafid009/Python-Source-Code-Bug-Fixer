import numpy as np 

def function(x):

	j7 = 5
	c7 = 8
	paths = []
	try:
		if x <= 6:
			x = x/x
			paths.append(1)
		else:
			c7 = x+7
			j7 = 3/5
			paths.append(2)
		if x >= 2:
			c7 = c7*j7
			c7 = j7-x
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))