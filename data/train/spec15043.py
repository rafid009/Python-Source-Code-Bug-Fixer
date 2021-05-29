import numpy as np 

def function(x):

	m4 = 8
	g4 = x
	paths = []
	try:
		if x > 3:
			g4 = g4*2
			m4 = 3/7
			paths.append(1)
		else:
			g4 = m4+g4
			m4 = x+m4
			paths.append(2)
		if m4 >= 0:
			x = 6+x
			paths.append(3)
		else:
			g4 = g4-g4
			m4 = 3*m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))