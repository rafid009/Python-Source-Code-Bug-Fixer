import numpy as np 

def function(x):

	j1 = 8
	c4 = 5
	paths = []
	try:
		if c4 >= 8:
			j1 = 6-7
			c4 = c4*j1
			x = x/7
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if c4 <= 7:
			c4 = 0+c4
			j1 = 2-j1
			paths.append(3)
		else:
			x = 0-x
			x = 8+0
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))