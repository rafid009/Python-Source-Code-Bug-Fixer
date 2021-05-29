import numpy as np 

def function(x):

	m1 = 6
	l6 = x
	paths = []
	try:
		if m1 < 3:
			m1 = m1+3
			paths.append(1)
		else:
			x = 8+x
			x = 8/x
			paths.append(2)
		if x >= 9:
			x = 0*x
			m1 = m1-1
			l6 = m1*6
			paths.append(3)
		else:
			m1 = 1*m1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))