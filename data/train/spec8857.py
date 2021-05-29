import numpy as np 

def function(x):

	m8 = x
	c3 = x
	paths = []
	try:
		if m8 <= 6:
			x = 9+1
			x = 6*6
			x = x/x
			paths.append(1)
		else:
			x = 1-2
			paths.append(2)
		if x > 0:
			m8 = m8/5
			m8 = m8+m8
			paths.append(3)
		else:
			m8 = c3-7
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		c3 = m8**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))