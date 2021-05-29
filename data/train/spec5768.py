import numpy as np 

def function(x):

	m8 = x
	g9 = 2
	paths = []
	try:
		if g9 <= 6:
			g9 = m8*m8
			g9 = 5/g9
			g9 = 1+g9
			paths.append(1)
		else:
			x = m8-7
			g9 = g9+0
			m8 = m8*g9
			paths.append(2)
		if g9 <= 1:
			m8 = x+1
			g9 = 0-5
			paths.append(3)
		else:
			m8 = m8/6
			x = x-1
			x = m8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))