import numpy as np 

def function(x):

	g1 = 3
	m5 = x
	paths = []
	try:
		if m5 <= 9:
			g1 = m5+g1
			g1 = 5*g1
			paths.append(1)
		else:
			g1 = 9/g1
			m5 = 3-3
			paths.append(2)
		if g1 >= 9:
			g1 = g1+g1
			paths.append(3)
		else:
			g1 = 7+5
			g1 = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))