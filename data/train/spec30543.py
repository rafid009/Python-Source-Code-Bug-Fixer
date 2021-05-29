import numpy as np 

def function(x):

	m7 = x
	h3 = 3
	paths = []
	try:
		if h3 <= 0:
			h3 = 3/h3
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x > 8:
			h3 = h3+8
			m7 = m7*m7
			paths.append(3)
		else:
			h3 = h3/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))