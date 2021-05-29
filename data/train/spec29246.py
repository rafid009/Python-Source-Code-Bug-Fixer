import numpy as np 

def function(x):

	c4 = x
	j7 = 2
	paths = []
	try:
		if x >= 9:
			j7 = j7+7
			paths.append(1)
		else:
			c4 = x+9
			c4 = c4*7
			paths.append(2)
		if c4 >= 2:
			j7 = j7*7
			c4 = 7*c4
			j7 = c4+2
			paths.append(3)
		else:
			j7 = c4*j7
			c4 = c4*9
			j7 = j7*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))