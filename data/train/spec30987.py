import numpy as np 

def function(x):

	m4 = 5
	g3 = x
	paths = []
	try:
		if x >= 1:
			m4 = m4/5
			g3 = g3*1
			m4 = m4/1
			paths.append(1)
		else:
			g3 = 2*g3
			m4 = 7-1
			x = 7+x
			paths.append(2)
		if g3 > 4:
			x = x*m4
			x = 3-g3
			m4 = m4-8
			paths.append(3)
		else:
			g3 = 0/g3
			m4 = 4-1
			m4 = m4+5
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