import numpy as np 

def function(x):

	c3 = x
	j7 = x
	paths = []
	try:
		if x < 1:
			j7 = j7+5
			x = c3-4
			j7 = 2*j7
			paths.append(1)
		else:
			x = x-c3
			c3 = c3-j7
			j7 = j7*3
			paths.append(2)
		if x <= 4:
			x = 9+4
			x = x-j7
			paths.append(3)
		else:
			j7 = 2+c3
			c3 = 7+8
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