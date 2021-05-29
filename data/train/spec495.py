import numpy as np 

def function(x):

	c2 = x
	m2 = x
	paths = []
	try:
		if x <= 1:
			x = c2+x
			c2 = c2-0
			paths.append(1)
		else:
			m2 = m2*0
			paths.append(2)
		if c2 < 9:
			c2 = c2-2
			m2 = m2+m2
			c2 = 1*6
			paths.append(3)
		else:
			c2 = 5/c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))