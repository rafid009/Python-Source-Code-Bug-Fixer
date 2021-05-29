import numpy as np 

def function(x):

	c8 = x
	m6 = 7
	paths = []
	try:
		if m6 <= 9:
			c8 = x-2
			m6 = x-0
			paths.append(1)
		else:
			m6 = m6+9
			m6 = 9+4
			paths.append(2)
		if m6 > 1:
			c8 = m6-c8
			c8 = 5*c8
			m6 = m6+4
			paths.append(3)
		else:
			m6 = c8+m6
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))