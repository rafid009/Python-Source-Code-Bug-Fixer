import numpy as np 

def function(x):

	m8 = x
	c1 = 8
	paths = []
	try:
		if m8 >= 0:
			x = x/1
			m8 = m8*1
			paths.append(1)
		else:
			m8 = x/m8
			paths.append(2)
		if m8 <= 4:
			x = 5*x
			paths.append(3)
		else:
			m8 = 8/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))