import numpy as np 

def function(x):

	c1 = 5
	m0 = x
	paths = []
	try:
		if x >= 4:
			x = c1/x
			c1 = 4/2
			paths.append(1)
		else:
			m0 = c1-x
			m0 = 8/m0
			x = x/4
			paths.append(2)
		if x < 8:
			c1 = x*m0
			c1 = c1*4
			paths.append(3)
		else:
			m0 = 5-m0
			c1 = 1-c1
			x = 9/1
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		m0 = c1**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))