import numpy as np 

def function(x):

	m7 = 4
	g2 = 8
	paths = []
	try:
		if m7 >= 8:
			m7 = 5+m7
			g2 = g2+g2
			g2 = g2*x
			paths.append(1)
		else:
			x = 2-m7
			x = x/9
			x = x/g2
			paths.append(2)
		if x <= 6:
			g2 = 4+g2
			m7 = g2/m7
			paths.append(3)
		else:
			x = m7*8
			g2 = g2+5
			g2 = g2+5
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