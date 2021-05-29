import numpy as np 

def function(x):

	c1 = 9
	m8 = x
	paths = []
	try:
		if c1 < 8:
			m8 = m8-m8
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x <= 8:
			c1 = 3/4
			paths.append(3)
		else:
			m8 = m8/m8
			m8 = c1-m8
			m8 = 4*m8
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))