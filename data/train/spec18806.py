import numpy as np 

def function(x):

	m3 = x
	e4 = 1
	paths = []
	try:
		if m3 <= 8:
			x = m3*m3
			x = 2/x
			paths.append(1)
		else:
			x = 9+x
			e4 = m3+6
			paths.append(2)
		if x > 6:
			m3 = 8-x
			paths.append(3)
		else:
			m3 = m3-m3
			e4 = e4*5
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))