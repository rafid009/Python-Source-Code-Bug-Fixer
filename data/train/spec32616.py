import numpy as np 

def function(x):

	g8 = 5
	m2 = 9
	paths = []
	try:
		if g8 <= 5:
			x = 7/x
			paths.append(1)
		else:
			m2 = m2+8
			g8 = x*2
			x = g8/5
			paths.append(2)
		if g8 > 4:
			g8 = g8/x
			paths.append(3)
		else:
			g8 = m2/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))