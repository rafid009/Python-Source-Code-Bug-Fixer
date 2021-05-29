import numpy as np 

def function(x):

	g4 = x
	m3 = x
	paths = []
	try:
		if m3 < 2:
			m3 = 1/x
			x = x-3
			paths.append(1)
		else:
			m3 = 3+3
			paths.append(2)
		if m3 > 5:
			m3 = m3/m3
			x = x+7
			paths.append(3)
		else:
			g4 = x*5
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		g4 = m3**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))