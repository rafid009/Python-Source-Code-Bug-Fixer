import numpy as np 

def function(x):

	m2 = 2
	c8 = 8
	paths = []
	try:
		if c8 >= 8:
			x = 1*9
			m2 = m2/4
			x = x+4
			paths.append(1)
		else:
			m2 = m2/c8
			x = x/x
			m2 = x*m2
			paths.append(2)
		if m2 <= 2:
			c8 = 2/6
			c8 = c8-x
			c8 = c8*5
			paths.append(3)
		else:
			m2 = 3/m2
			c8 = c8+m2
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