import numpy as np 

def function(x):

	c1 = x
	m9 = 4
	paths = []
	try:
		if c1 > 5:
			x = x*9
			c1 = 0*9
			x = c1-7
			paths.append(1)
		else:
			m9 = m9+7
			c1 = c1/1
			c1 = c1+x
			paths.append(2)
		if c1 >= 8:
			c1 = c1/x
			m9 = m9+5
			m9 = 6-x
			paths.append(3)
		else:
			m9 = m9+x
			m9 = 3-m9
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		m9 = c1**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))