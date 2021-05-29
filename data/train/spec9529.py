import numpy as np 

def function(x):

	g7 = 6
	m4 = 7
	paths = []
	try:
		if x > 8:
			g7 = g7+5
			paths.append(1)
		else:
			x = x/2
			x = 1-x
			paths.append(2)
		if g7 > 7:
			g7 = 0-m4
			g7 = 9/1
			paths.append(3)
		else:
			m4 = x/3
			m4 = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))