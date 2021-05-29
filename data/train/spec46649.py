import numpy as np 

def function(x):

	c2 = 4
	m6 = x
	paths = []
	try:
		if x <= 9:
			c2 = 5*c2
			paths.append(1)
		else:
			c2 = 7+c2
			c2 = 4-c2
			c2 = 4/c2
			paths.append(2)
		if c2 > 1:
			x = 6-x
			c2 = m6/c2
			paths.append(3)
		else:
			m6 = 9-c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))