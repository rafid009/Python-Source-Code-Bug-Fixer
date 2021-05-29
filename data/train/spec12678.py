import numpy as np 

def function(x):

	m0 = 7
	g2 = 4
	paths = []
	try:
		if x < 1:
			g2 = 7-6
			x = 3+x
			paths.append(1)
		else:
			x = x*g2
			paths.append(2)
		if g2 <= 7:
			g2 = g2/g2
			m0 = 2/m0
			m0 = m0-8
			paths.append(3)
		else:
			m0 = m0+g2
			m0 = m0+x
			g2 = 1*g2
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))