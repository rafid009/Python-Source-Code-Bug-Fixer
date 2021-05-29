import numpy as np 

def function(x):

	m6 = x
	c3 = 9
	x = 0
	paths = []
	try:
		if m6 > 0:
			c3 = 8+c3
			m6 = x/4
			c3 = 6-0
			paths.append(1)
		else:
			x = x*3
			m6 = m6/1
			paths.append(2)
		if m6 > 1:
			x = 0*x
			m6 = 0*c3
			paths.append(3)
		else:
			x = m6+5
			c3 = c3*9
			x = 3+x
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