import numpy as np 

def function(x):

	m7 = 3
	g4 = 2
	paths = []
	try:
		if m7 < 4:
			m7 = g4-9
			m7 = 2*m7
			paths.append(1)
		else:
			m7 = 7*8
			paths.append(2)
		if g4 <= 7:
			x = x-m7
			paths.append(3)
		else:
			g4 = g4+7
			m7 = 2-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))