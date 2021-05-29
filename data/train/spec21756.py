import numpy as np 

def function(x):

	m9 = 6
	l7 = x
	paths = []
	try:
		if m9 > 3:
			l7 = l7/x
			l7 = l7+5
			paths.append(1)
		else:
			m9 = m9-7
			m9 = m9+m9
			paths.append(2)
		if m9 > 2:
			m9 = m9*8
			x = l7-x
			paths.append(3)
		else:
			m9 = 4+m9
			l7 = 8/3
			l7 = l7+l7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))