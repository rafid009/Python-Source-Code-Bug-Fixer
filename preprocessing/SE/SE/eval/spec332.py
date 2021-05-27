import numpy as np 

def function(x):

	r9 = 1
	m8 = x
	paths = []
	try:
		if x >= 5:
			r9 = x+8
			paths.append(1)
		else:
			x = m8+x
			paths.append(2)
		if x >= 6:
			r9 = r9*r9
			r9 = r9+2
			m8 = r9-4
			paths.append(3)
		else:
			r9 = r9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))