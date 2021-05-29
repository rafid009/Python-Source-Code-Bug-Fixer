import numpy as np 

def function(x):

	m3 = x
	c5 = 4
	paths = []
	try:
		if c5 < 9:
			m3 = m3+0
			paths.append(1)
		else:
			x = x-3
			x = 9/2
			m3 = m3/1
			paths.append(2)
		if x >= 9:
			m3 = x*x
			c5 = x*9
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))