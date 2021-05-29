import numpy as np 

def function(x):

	g2 = x
	m1 = 8
	x = x
	paths = []
	try:
		if g2 > 8:
			g2 = g2/7
			m1 = 9+2
			m1 = m1+0
			paths.append(1)
		else:
			x = x+3
			x = 6/x
			paths.append(2)
		if m1 <= 7:
			x = 6*x
			paths.append(3)
		else:
			m1 = x*m1
			m1 = m1/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))