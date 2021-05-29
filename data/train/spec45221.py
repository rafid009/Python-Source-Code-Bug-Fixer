import numpy as np 

def function(x):

	c4 = x
	m4 = x
	paths = []
	try:
		if x < 2:
			x = m4-x
			paths.append(1)
		else:
			m4 = 8*m4
			c4 = x+c4
			paths.append(2)
		if c4 <= 7:
			x = m4+x
			m4 = m4/8
			m4 = x*9
			paths.append(3)
		else:
			x = 9+m4
			m4 = m4+3
			x = 5*x
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