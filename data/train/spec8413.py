import numpy as np 

def function(x):

	m9 = 3
	p0 = x
	paths = []
	try:
		if x >= 8:
			x = 0-5
			paths.append(1)
		else:
			x = 1/x
			m9 = m9*4
			m9 = 8/8
			paths.append(2)
		if x > 3:
			m9 = m9/3
			paths.append(3)
		else:
			m9 = m9*4
			m9 = m9-8
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))