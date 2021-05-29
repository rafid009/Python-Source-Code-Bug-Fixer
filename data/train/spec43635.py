import numpy as np 

def function(x):

	m2 = x
	c6 = x
	paths = []
	try:
		if m2 >= 1:
			c6 = x+4
			m2 = m2/1
			m2 = m2/6
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if x <= 3:
			c6 = 5-c6
			m2 = m2+7
			paths.append(3)
		else:
			m2 = 1-m2
			m2 = 9-6
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