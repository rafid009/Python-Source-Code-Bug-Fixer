import numpy as np 

def function(x):

	c7 = x
	m4 = 5
	paths = []
	try:
		if c7 <= 4:
			m4 = c7*6
			x = x+c7
			c7 = m4*x
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if m4 > 2:
			x = x-2
			x = 5+5
			c7 = 5-2
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))