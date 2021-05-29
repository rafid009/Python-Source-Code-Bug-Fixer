import numpy as np 

def function(x):

	g7 = 9
	m0 = x
	paths = []
	try:
		if x <= 3:
			m0 = m0+2
			g7 = g7*0
			paths.append(1)
		else:
			m0 = g7+4
			m0 = 2*9
			paths.append(2)
		if x <= 1:
			x = 3*x
			x = x-1
			g7 = g7*5
			paths.append(3)
		else:
			m0 = m0/1
			m0 = m0+0
			g7 = g7/8
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))