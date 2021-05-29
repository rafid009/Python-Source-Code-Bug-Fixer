import numpy as np 

def function(x):

	m7 = x
	g8 = 9
	paths = []
	try:
		if m7 >= 4:
			x = x*x
			paths.append(1)
		else:
			m7 = m7-9
			paths.append(2)
		if g8 > 1:
			m7 = 6*m7
			g8 = 8-3
			g8 = g8-x
			paths.append(3)
		else:
			g8 = x*g8
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