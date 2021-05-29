import numpy as np 

def function(x):

	c2 = x
	m8 = 1
	paths = []
	try:
		if m8 >= 0:
			m8 = x+9
			m8 = x+m8
			paths.append(1)
		else:
			x = 5-1
			c2 = c2/m8
			paths.append(2)
		if x < 3:
			x = m8/4
			m8 = 5-m8
			x = m8/7
			paths.append(3)
		else:
			c2 = c2/7
			x = c2/x
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))