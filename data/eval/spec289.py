import numpy as np 

def function(x):

	m9 = x
	m0 = x
	x = 7
	paths = []
	try:
		if m0 <= 0:
			m9 = m9+m9
			m9 = x*2
			m0 = m0+6
			paths.append(1)
		else:
			m0 = 7/6
			x = x+7
			paths.append(2)
		if m9 < 8:
			x = m0-5
			x = 5*x
			paths.append(3)
		else:
			x = m9-0
			m9 = 1-m0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))