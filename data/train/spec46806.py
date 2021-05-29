import numpy as np 

def function(x):

	w8 = x
	m9 = x
	paths = []
	try:
		if w8 < 0:
			m9 = 1/m9
			x = 3/x
			w8 = m9-6
			paths.append(1)
		else:
			w8 = w8*7
			x = 9+x
			paths.append(2)
		if x > 8:
			w8 = m9-6
			m9 = w8/7
			m9 = m9-w8
			paths.append(3)
		else:
			x = x+x
			m9 = 1*5
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