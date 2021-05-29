import numpy as np 

def function(x):

	c4 = x
	m7 = x
	paths = []
	try:
		if m7 > 8:
			c4 = 0+8
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if c4 <= 9:
			m7 = m7+6
			paths.append(3)
		else:
			c4 = c4-m7
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