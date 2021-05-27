import numpy as np 

def function(x):

	h2 = x
	m3 = 5
	paths = []
	try:
		if h2 <= 2:
			m3 = 7/7
			x = x/h2
			paths.append(1)
		else:
			m3 = m3-m3
			paths.append(2)
		if h2 > 6:
			h2 = h2*3
			m3 = 7+1
			x = h2*7
			paths.append(3)
		else:
			x = 3-x
			h2 = 9+h2
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))