import numpy as np 

def function(x):

	g5 = 8
	m5 = 5
	paths = []
	try:
		if m5 >= 6:
			g5 = g5-m5
			paths.append(1)
		else:
			m5 = 4-m5
			x = g5+x
			g5 = x+2
			paths.append(2)
		if g5 < 3:
			g5 = m5/m5
			paths.append(3)
		else:
			g5 = m5-0
			x = x*x
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