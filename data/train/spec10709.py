import numpy as np 

def function(x):

	m7 = 7
	g8 = x
	paths = []
	try:
		if x > 2:
			m7 = m7/x
			m7 = m7+4
			paths.append(1)
		else:
			x = 4-x
			x = 6+x
			paths.append(2)
		if g8 < 9:
			m7 = m7*6
			paths.append(3)
		else:
			g8 = g8*4
			x = x/g8
			x = x/x
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		m7 = g8**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))