import numpy as np 

def function(x):

	e9 = x
	c1 = 2
	x = 6
	paths = []
	try:
		if e9 <= 9:
			x = x*0
			x = e9-5
			paths.append(1)
		else:
			e9 = e9-4
			e9 = 5*e9
			paths.append(2)
		if e9 > 8:
			e9 = x*6
			e9 = 0*e9
			paths.append(3)
		else:
			c1 = c1*e9
			e9 = 1-e9
			c1 = 0*c1
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		c1 = e9**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))