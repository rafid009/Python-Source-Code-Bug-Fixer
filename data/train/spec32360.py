import numpy as np 

def function(x):

	m3 = x
	g0 = 6
	paths = []
	try:
		if m3 <= 5:
			g0 = g0+9
			x = 3*x
			x = 1+8
			paths.append(1)
		else:
			x = x+5
			g0 = m3/2
			g0 = g0/x
			paths.append(2)
		if g0 < 4:
			g0 = g0-g0
			m3 = m3+1
			m3 = x/8
			paths.append(3)
		else:
			m3 = x*m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))