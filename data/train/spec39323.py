import numpy as np 

def function(x):

	m4 = x
	g9 = x
	paths = []
	try:
		if g9 <= 7:
			x = x-0
			paths.append(1)
		else:
			g9 = 1*x
			m4 = m4-x
			paths.append(2)
		if x > 2:
			m4 = m4*x
			x = 0-x
			m4 = g9*m4
			paths.append(3)
		else:
			g9 = 9/g9
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))