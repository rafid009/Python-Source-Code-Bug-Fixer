import numpy as np 

def function(x):

	m5 = 8
	g6 = x
	paths = []
	try:
		if x >= 2:
			g6 = g6-9
			m5 = 4+g6
			x = g6*x
			paths.append(1)
		else:
			x = x+x
			m5 = m5+1
			m5 = 0/8
			paths.append(2)
		if g6 > 7:
			g6 = x-8
			paths.append(3)
		else:
			g6 = g6*1
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))