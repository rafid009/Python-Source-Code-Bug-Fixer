import numpy as np 

def function(x):

	g0 = x
	m2 = 2
	paths = []
	try:
		if x <= 7:
			m2 = 6-g0
			g0 = 2*g0
			paths.append(1)
		else:
			m2 = 6/x
			g0 = 4/g0
			paths.append(2)
		if x <= 7:
			g0 = g0*2
			x = x/x
			g0 = 3*9
			paths.append(3)
		else:
			m2 = m2*2
			x = g0/m2
			m2 = m2+m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		g0 = m2**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))