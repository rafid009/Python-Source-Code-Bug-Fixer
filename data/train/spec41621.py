import numpy as np 

def function(x):

	m9 = 9
	l4 = 6
	paths = []
	try:
		if x <= 4:
			m9 = 5*m9
			m9 = 2+6
			l4 = l4+3
			paths.append(1)
		else:
			x = x*x
			m9 = m9+m9
			m9 = 4/m9
			paths.append(2)
		if m9 < 2:
			m9 = m9-x
			paths.append(3)
		else:
			l4 = 9*5
			l4 = l4+m9
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