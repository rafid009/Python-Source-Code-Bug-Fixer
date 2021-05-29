import numpy as np 

def function(x):

	c7 = 2
	j1 = 0
	paths = []
	try:
		if c7 <= 2:
			j1 = 1-4
			paths.append(1)
		else:
			c7 = 6+c7
			j1 = 2+j1
			paths.append(2)
		if j1 > 9:
			j1 = c7/j1
			paths.append(3)
		else:
			c7 = c7/7
			c7 = j1*c7
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