import numpy as np 

def function(x):

	m5 = x
	g2 = 0
	paths = []
	try:
		if g2 < 0:
			g2 = g2*1
			m5 = 9*m5
			x = x+m5
			paths.append(1)
		else:
			m5 = 1/9
			m5 = m5+m5
			g2 = g2-x
			paths.append(2)
		if x > 2:
			g2 = g2-8
			m5 = 0/m5
			paths.append(3)
		else:
			m5 = 4*m5
			g2 = 8/g2
			g2 = 2+g2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		m5 = g2**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))