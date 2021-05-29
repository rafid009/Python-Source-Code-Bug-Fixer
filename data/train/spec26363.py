import numpy as np 

def function(x):

	g2 = 1
	m3 = 1
	paths = []
	try:
		if m3 >= 4:
			m3 = 5-m3
			g2 = m3+8
			m3 = 1-m3
			paths.append(1)
		else:
			x = x-4
			g2 = x-g2
			paths.append(2)
		if g2 <= 8:
			m3 = m3/8
			paths.append(3)
		else:
			m3 = m3*6
			m3 = 4+g2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		m3 = g2**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))