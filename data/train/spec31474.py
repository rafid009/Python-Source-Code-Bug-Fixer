import numpy as np 

def function(x):

	c4 = x
	m3 = x
	paths = []
	try:
		if x >= 0:
			m3 = 2+0
			paths.append(1)
		else:
			x = c4-1
			c4 = x*m3
			paths.append(2)
		if c4 >= 7:
			x = 1+x
			c4 = x-c4
			paths.append(3)
		else:
			m3 = 2+m3
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		m3 = c4**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))