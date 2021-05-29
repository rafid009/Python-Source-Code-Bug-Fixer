import numpy as np 

def function(x):

	l6 = 4
	m7 = 5
	paths = []
	try:
		if m7 <= 8:
			l6 = l6*6
			paths.append(1)
		else:
			l6 = 6*l6
			x = 0*x
			paths.append(2)
		if m7 >= 8:
			m7 = m7+6
			m7 = m7*m7
			paths.append(3)
		else:
			l6 = l6/m7
			m7 = 9+m7
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))