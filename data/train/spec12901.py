import numpy as np 

def function(x):

	h0 = 0
	m9 = 9
	paths = []
	try:
		if m9 >= 7:
			m9 = 0/7
			paths.append(1)
		else:
			m9 = 4/9
			x = 0-x
			h0 = h0+x
			paths.append(2)
		if m9 <= 7:
			m9 = h0/8
			h0 = h0/8
			h0 = h0-9
			paths.append(3)
		else:
			x = x+3
			x = h0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))