import numpy as np 

def function(x):

	c3 = 8
	m4 = x
	x = x
	paths = []
	try:
		if c3 <= 1:
			c3 = c3-7
			paths.append(1)
		else:
			m4 = 6/9
			c3 = x/6
			paths.append(2)
		if x <= 8:
			m4 = m4/x
			m4 = m4/5
			paths.append(3)
		else:
			c3 = 0*c3
			x = c3-c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		m4 = c3**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))