import numpy as np 

def function(x):

	i0 = 8
	m9 = 6
	paths = []
	try:
		if x <= 1:
			m9 = 2*1
			i0 = 8/7
			paths.append(1)
		else:
			m9 = x*m9
			m9 = m9/i0
			x = 1/6
			paths.append(2)
		if m9 < 0:
			x = 3-x
			paths.append(3)
		else:
			m9 = m9*x
			i0 = m9*6
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