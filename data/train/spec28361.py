import numpy as np 

def function(x):

	e7 = 6
	c1 = x
	paths = []
	try:
		if c1 <= 9:
			x = 1-x
			x = 5*8
			paths.append(1)
		else:
			c1 = c1/7
			c1 = c1*8
			paths.append(2)
		if x <= 8:
			c1 = c1/e7
			e7 = c1+x
			x = x+0
			paths.append(3)
		else:
			x = x/4
			x = 6-8
			e7 = e7-8
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		e7 = c1**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))