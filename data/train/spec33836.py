import numpy as np 

def function(x):

	m0 = x
	c4 = x
	paths = []
	try:
		if x < 0:
			c4 = 5/x
			x = 0+4
			paths.append(1)
		else:
			m0 = m0/7
			paths.append(2)
		if m0 < 7:
			c4 = c4/6
			x = 5*x
			paths.append(3)
		else:
			c4 = c4*m0
			c4 = 9+2
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		m0 = c4**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))