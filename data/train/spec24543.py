import numpy as np 

def function(x):

	m1 = x
	g7 = 3
	x = x
	paths = []
	try:
		if m1 >= 3:
			m1 = m1-m1
			paths.append(1)
		else:
			m1 = m1+0
			m1 = x+9
			paths.append(2)
		if x >= 6:
			m1 = 4*m1
			x = x*2
			m1 = 5+m1
			paths.append(3)
		else:
			g7 = g7*2
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		g7 = m1**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))