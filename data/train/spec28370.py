import numpy as np 

def function(x):

	m3 = x
	g2 = x
	paths = []
	try:
		if x >= 9:
			g2 = g2+0
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if m3 >= 3:
			g2 = g2/m3
			paths.append(3)
		else:
			m3 = 0-1
			m3 = 8/m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))