import numpy as np 

def function(x):

	m1 = 6
	g1 = 0
	paths = []
	try:
		if g1 < 7:
			g1 = g1+3
			m1 = m1*x
			paths.append(1)
		else:
			g1 = 8-6
			g1 = 3*7
			g1 = g1+3
			paths.append(2)
		if m1 <= 1:
			g1 = g1/3
			g1 = x/g1
			g1 = g1/1
			paths.append(3)
		else:
			g1 = 5/g1
			m1 = m1-4
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))