import numpy as np 

def function(x):

	l8 = x
	m4 = x
	paths = []
	try:
		if l8 > 8:
			m4 = m4*m4
			m4 = 4+4
			paths.append(1)
		else:
			m4 = 1+m4
			paths.append(2)
		if l8 <= 4:
			x = l8/x
			m4 = 9*m4
			paths.append(3)
		else:
			l8 = x+l8
			x = 8-3
			x = 7-6
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		l8 = m4**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))