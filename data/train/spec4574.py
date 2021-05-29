import numpy as np 

def function(x):

	m6 = 5
	g4 = 5
	paths = []
	try:
		if g4 < 1:
			g4 = 6+g4
			x = g4+x
			paths.append(1)
		else:
			g4 = 9+x
			paths.append(2)
		if m6 > 7:
			x = x/7
			g4 = g4+m6
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		m6 = g4**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))