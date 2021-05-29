import numpy as np 

def function(x):

	c8 = 4
	m2 = 1
	paths = []
	try:
		if c8 > 8:
			m2 = m2*8
			x = 1+x
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x >= 3:
			x = x-4
			x = x/2
			c8 = 5*m2
			paths.append(3)
		else:
			c8 = 5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))