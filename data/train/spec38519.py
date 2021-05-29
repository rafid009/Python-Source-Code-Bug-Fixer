import numpy as np 

def function(x):

	m9 = x
	l9 = 5
	x = x
	paths = []
	try:
		if m9 <= 2:
			l9 = 8+3
			paths.append(1)
		else:
			x = 0-x
			m9 = 5/m9
			m9 = m9+m9
			paths.append(2)
		if m9 <= 0:
			x = 9*x
			paths.append(3)
		else:
			m9 = 4+m9
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