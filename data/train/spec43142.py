import numpy as np 

def function(x):

	m9 = x
	h7 = 1
	paths = []
	try:
		if x <= 5:
			m9 = 1+m9
			paths.append(1)
		else:
			m9 = m9*x
			paths.append(2)
		if x >= 6:
			m9 = m9-1
			x = x/8
			paths.append(3)
		else:
			h7 = x*8
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