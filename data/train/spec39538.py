import numpy as np 

def function(x):

	h0 = 7
	m5 = x
	paths = []
	try:
		if m5 >= 9:
			h0 = 7+h0
			m5 = 7-m5
			paths.append(1)
		else:
			x = 6-x
			h0 = 2/x
			x = 6/x
			paths.append(2)
		if x >= 5:
			x = x/2
			h0 = m5+h0
			paths.append(3)
		else:
			x = 0-x
			m5 = m5*7
			m5 = m5-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))