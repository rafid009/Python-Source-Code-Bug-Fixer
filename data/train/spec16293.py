import numpy as np 

def function(x):

	m8 = x
	g9 = 9
	paths = []
	try:
		if g9 >= 7:
			g9 = g9-3
			m8 = 2*m8
			paths.append(1)
		else:
			x = g9-g9
			x = 7+x
			paths.append(2)
		if m8 <= 8:
			m8 = g9-m8
			paths.append(3)
		else:
			x = 0+7
			m8 = 1*m8
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		g9 = m8**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))