import numpy as np 

def function(x):

	y6 = x
	m3 = x
	paths = []
	try:
		if x < 5:
			x = 0-x
			paths.append(1)
		else:
			m3 = m3+5
			x = x*8
			paths.append(2)
		if x >= 9:
			m3 = m3-3
			x = 0-3
			m3 = m3-x
			paths.append(3)
		else:
			y6 = y6+m3
			y6 = y6+y6
			y6 = y6-6
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