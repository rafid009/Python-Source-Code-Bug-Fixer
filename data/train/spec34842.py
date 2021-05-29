import numpy as np 

def function(x):

	g5 = 9
	m4 = 6
	x = x
	paths = []
	try:
		if m4 < 6:
			g5 = g5+x
			g5 = g5-4
			paths.append(1)
		else:
			m4 = m4+6
			paths.append(2)
		if g5 >= 8:
			x = 2-x
			paths.append(3)
		else:
			m4 = g5-m4
			x = 4*x
			g5 = 6/g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))