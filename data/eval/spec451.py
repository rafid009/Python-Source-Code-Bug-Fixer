import numpy as np 

def function(x):

	c8 = 3
	m5 = 9
	paths = []
	try:
		if m5 >= 0:
			m5 = x+2
			m5 = 0/1
			c8 = 8*c8
			paths.append(1)
		else:
			m5 = 8/3
			paths.append(2)
		if x < 1:
			x = x+c8
			c8 = c8*x
			paths.append(3)
		else:
			m5 = m5*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))