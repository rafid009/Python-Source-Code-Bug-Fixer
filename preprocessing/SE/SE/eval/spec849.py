import numpy as np 

def function(x):

	m2 = 0
	c1 = 7
	paths = []
	try:
		if m2 <= 3:
			m2 = m2+2
			paths.append(1)
		else:
			m2 = m2+1
			m2 = m2/x
			paths.append(2)
		if x < 4:
			c1 = c1-7
			paths.append(3)
		else:
			x = c1*x
			c1 = 6/m2
			x = x-2
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