import numpy as np 

def function(x):

	c1 = 8
	m1 = x
	paths = []
	try:
		if c1 < 6:
			c1 = 8/m1
			paths.append(1)
		else:
			m1 = 9-m1
			x = x-8
			paths.append(2)
		if m1 >= 3:
			x = m1/1
			paths.append(3)
		else:
			x = x-m1
			c1 = c1-m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))