import numpy as np 

def function(x):

	h9 = 8
	m1 = x
	x = 9
	paths = []
	try:
		if m1 < 6:
			m1 = m1-h9
			h9 = 9/h9
			m1 = m1/4
			paths.append(1)
		else:
			m1 = m1/x
			x = h9-1
			paths.append(2)
		if x >= 6:
			x = x*x
			paths.append(3)
		else:
			x = h9+x
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))