import numpy as np 

def function(x):

	c7 = x
	j1 = 1
	paths = []
	try:
		if x <= 7:
			x = c7*5
			j1 = j1+0
			x = 2+x
			paths.append(1)
		else:
			j1 = 8-c7
			j1 = j1/3
			c7 = 5+1
			paths.append(2)
		if j1 <= 0:
			x = 3/7
			c7 = x/8
			x = x-c7
			paths.append(3)
		else:
			j1 = j1*7
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		c7 = j1**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))