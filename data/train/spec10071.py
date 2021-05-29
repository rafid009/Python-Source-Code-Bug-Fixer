import numpy as np 

def function(x):

	h9 = 1
	m2 = x
	paths = []
	try:
		if m2 < 7:
			x = 7/8
			m2 = m2+m2
			paths.append(1)
		else:
			h9 = 6-x
			m2 = 2+5
			paths.append(2)
		if h9 <= 7:
			m2 = x-m2
			x = h9-3
			x = 6*4
			paths.append(3)
		else:
			x = 0-4
			m2 = m2/7
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))