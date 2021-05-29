import numpy as np 

def function(x):

	c1 = 8
	e0 = x
	paths = []
	try:
		if c1 > 5:
			e0 = e0+7
			paths.append(1)
		else:
			c1 = 1*c1
			e0 = 7/e0
			c1 = c1+x
			paths.append(2)
		if e0 < 1:
			x = x+0
			x = 9-x
			x = 2+x
			paths.append(3)
		else:
			e0 = e0-e0
			c1 = 3*x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		e0 = c1**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))