import numpy as np 

def function(x):

	c3 = 0
	a6 = x
	paths = []
	try:
		if c3 > 6:
			a6 = a6/c3
			c3 = 7*x
			c3 = c3*4
			paths.append(1)
		else:
			a6 = a6/5
			a6 = a6+1
			x = x/2
			paths.append(2)
		if x < 4:
			x = 9/x
			paths.append(3)
		else:
			c3 = c3*x
			a6 = 1-c3
			x = a6-x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))