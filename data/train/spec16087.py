import numpy as np 

def function(x):

	g8 = 9
	m8 = 4
	paths = []
	try:
		if x < 4:
			m8 = g8/x
			g8 = m8*g8
			g8 = x+g8
			paths.append(1)
		else:
			g8 = 7-g8
			x = x+8
			m8 = 1/m8
			paths.append(2)
		if g8 >= 6:
			x = 3/7
			paths.append(3)
		else:
			x = 5-x
			m8 = m8+9
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))