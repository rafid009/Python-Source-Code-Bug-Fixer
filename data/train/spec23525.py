import numpy as np 

def function(x):

	m0 = x
	l6 = x
	paths = []
	try:
		if x >= 9:
			x = m0+l6
			l6 = 1*1
			x = x+3
			paths.append(1)
		else:
			m0 = 5+m0
			x = x+6
			x = 4-m0
			paths.append(2)
		if l6 >= 5:
			x = x+3
			l6 = 6/l6
			l6 = 9+l6
			paths.append(3)
		else:
			l6 = m0-2
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))