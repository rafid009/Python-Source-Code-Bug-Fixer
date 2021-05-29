import numpy as np 

def function(x):

	m6 = 4
	h4 = 5
	paths = []
	try:
		if m6 < 9:
			m6 = 3-x
			x = x-7
			paths.append(1)
		else:
			m6 = m6/9
			h4 = h4+x
			m6 = 5-x
			paths.append(2)
		if h4 > 2:
			m6 = m6+3
			h4 = h4/1
			h4 = h4+2
			paths.append(3)
		else:
			m6 = 4/3
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