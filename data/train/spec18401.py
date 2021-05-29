import numpy as np 

def function(x):

	c7 = x
	p1 = x
	x = 6
	paths = []
	try:
		if p1 <= 0:
			c7 = 3*c7
			paths.append(1)
		else:
			p1 = c7/p1
			paths.append(2)
		if p1 >= 8:
			x = 9*7
			x = c7-x
			p1 = 6/p1
			paths.append(3)
		else:
			x = x/5
			x = 1/x
			c7 = c7-4
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))