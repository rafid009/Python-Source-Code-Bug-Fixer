import numpy as np 

def function(x):

	g6 = 5
	m8 = 9
	paths = []
	try:
		if m8 < 0:
			m8 = 8-m8
			paths.append(1)
		else:
			g6 = g6+g6
			g6 = g6-x
			paths.append(2)
		if x > 5:
			m8 = m8*m8
			paths.append(3)
		else:
			m8 = x-m8
			m8 = m8/x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))