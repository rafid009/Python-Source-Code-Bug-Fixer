import numpy as np 

def function(x):

	g7 = 4
	m7 = 4
	paths = []
	try:
		if g7 <= 3:
			x = 4/x
			paths.append(1)
		else:
			m7 = g7*3
			paths.append(2)
		if x > 9:
			g7 = x/g7
			paths.append(3)
		else:
			g7 = x/1
			m7 = m7/3
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		m7 = g7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))