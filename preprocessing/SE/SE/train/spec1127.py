import numpy as np 

def function(x):

	g8 = 4
	m2 = 5
	x = x
	paths = []
	try:
		if g8 <= 6:
			m2 = 1-m2
			x = x/4
			x = m2-x
			paths.append(1)
		else:
			x = 1+x
			m2 = m2+7
			paths.append(2)
		if x > 0:
			x = x-3
			g8 = 8+g8
			m2 = 5+m2
			paths.append(3)
		else:
			m2 = m2-m2
			x = 8/4
			m2 = g8-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))