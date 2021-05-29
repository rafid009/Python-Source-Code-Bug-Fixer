import numpy as np 

def function(x):

	m6 = 3
	g7 = x
	paths = []
	try:
		if g7 > 5:
			m6 = m6-8
			x = x+x
			paths.append(1)
		else:
			m6 = m6+g7
			paths.append(2)
		if x <= 6:
			g7 = g7*3
			m6 = m6*8
			g7 = g7/3
			paths.append(3)
		else:
			g7 = g7*6
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))