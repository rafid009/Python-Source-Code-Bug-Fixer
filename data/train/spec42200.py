import numpy as np 

def function(x):

	l6 = x
	m6 = 4
	paths = []
	try:
		if x > 0:
			m6 = l6/x
			l6 = m6+6
			paths.append(1)
		else:
			l6 = 5/l6
			m6 = 0+3
			x = x+6
			paths.append(2)
		if l6 < 7:
			m6 = m6/4
			paths.append(3)
		else:
			l6 = l6/4
			m6 = 7*l6
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