import numpy as np 

def function(x):

	m3 = x
	x3 = x
	paths = []
	try:
		if x < 6:
			x = x/8
			m3 = m3-9
			m3 = x-m3
			paths.append(1)
		else:
			m3 = 0-m3
			x = 0-0
			m3 = 3/m3
			paths.append(2)
		if x >= 9:
			m3 = 7-x
			paths.append(3)
		else:
			m3 = m3-0
			x3 = 1+x3
			x = x+0
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