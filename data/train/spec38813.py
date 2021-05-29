import numpy as np 

def function(x):

	g8 = x
	m3 = x
	paths = []
	try:
		if x >= 7:
			g8 = g8/6
			g8 = g8-5
			g8 = g8/x
			paths.append(1)
		else:
			g8 = g8-8
			g8 = g8*x
			m3 = 5+5
			paths.append(2)
		if m3 >= 4:
			m3 = m3-3
			m3 = g8/m3
			m3 = m3/g8
			paths.append(3)
		else:
			g8 = g8/3
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))