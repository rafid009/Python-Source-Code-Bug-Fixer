import numpy as np 

def function(x):

	m4 = x
	c7 = x
	paths = []
	try:
		if x >= 1:
			m4 = c7+m4
			m4 = 9/m4
			c7 = c7/1
			paths.append(1)
		else:
			c7 = x*c7
			paths.append(2)
		if c7 < 1:
			m4 = m4/m4
			m4 = m4*6
			m4 = m4+c7
			paths.append(3)
		else:
			x = 3-4
			c7 = c7*9
			x = x*2
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))