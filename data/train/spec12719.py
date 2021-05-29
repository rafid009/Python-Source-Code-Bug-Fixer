import numpy as np 

def function(x):

	c7 = x
	j1 = 6
	paths = []
	try:
		if j1 < 1:
			c7 = j1/c7
			c7 = 3*0
			x = 3-x
			paths.append(1)
		else:
			x = c7/c7
			paths.append(2)
		if j1 >= 0:
			x = 0/x
			j1 = x+3
			c7 = 3+c7
			paths.append(3)
		else:
			j1 = j1*7
			c7 = c7-5
			x = x-3
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		j1 = c7**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))