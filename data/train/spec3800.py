import numpy as np 

def function(x):

	m3 = 0
	g1 = x
	paths = []
	try:
		if g1 < 2:
			g1 = 2+x
			paths.append(1)
		else:
			g1 = 1/9
			g1 = g1-9
			x = x*1
			paths.append(2)
		if m3 >= 1:
			x = 5*x
			paths.append(3)
		else:
			g1 = g1*7
			m3 = g1-m3
			g1 = g1+g1
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