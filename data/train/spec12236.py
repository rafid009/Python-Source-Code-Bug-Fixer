import numpy as np 

def function(x):

	m2 = x
	c4 = x
	paths = []
	try:
		if m2 >= 9:
			c4 = 4*4
			paths.append(1)
		else:
			m2 = 0-5
			c4 = c4*9
			paths.append(2)
		if x <= 6:
			m2 = m2*4
			paths.append(3)
		else:
			x = m2+x
			c4 = m2/c4
			c4 = 8*c4
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))