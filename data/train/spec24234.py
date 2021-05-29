import numpy as np 

def function(x):

	g8 = x
	m3 = 0
	paths = []
	try:
		if x <= 6:
			x = 7*x
			paths.append(1)
		else:
			m3 = 4-m3
			g8 = x*5
			paths.append(2)
		if g8 >= 0:
			g8 = 8/g8
			g8 = g8+1
			x = 6*x
			paths.append(3)
		else:
			m3 = m3*7
			g8 = g8/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))