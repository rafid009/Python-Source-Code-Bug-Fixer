import numpy as np 

def function(x):

	c7 = 6
	m8 = 7
	paths = []
	try:
		if m8 >= 7:
			m8 = m8*4
			paths.append(1)
		else:
			c7 = 8*1
			x = x+c7
			paths.append(2)
		if x <= 9:
			x = x-7
			x = x/6
			m8 = m8-2
			paths.append(3)
		else:
			x = x+6
			m8 = m8-3
			m8 = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))