import numpy as np 

def function(x):

	m7 = x
	c9 = x
	paths = []
	try:
		if x < 2:
			x = 6*2
			paths.append(1)
		else:
			m7 = c9+2
			paths.append(2)
		if c9 > 5:
			c9 = x-1
			c9 = c9*9
			paths.append(3)
		else:
			x = 9+c9
			x = 1+x
			x = x/1
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))