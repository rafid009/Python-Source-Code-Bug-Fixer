import numpy as np 

def function(x):

	c6 = x
	m6 = x
	paths = []
	try:
		if m6 > 8:
			m6 = 0-m6
			paths.append(1)
		else:
			m6 = m6*5
			x = 6*2
			paths.append(2)
		if m6 < 6:
			x = 0+x
			paths.append(3)
		else:
			m6 = x*m6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))