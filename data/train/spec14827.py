import numpy as np 

def function(x):

	m6 = 0
	h8 = 3
	paths = []
	try:
		if h8 <= 5:
			h8 = 7/h8
			x = 2*x
			h8 = h8-7
			paths.append(1)
		else:
			x = 2+2
			x = m6+x
			m6 = x+x
			paths.append(2)
		if x < 1:
			h8 = h8+x
			paths.append(3)
		else:
			m6 = m6*4
			h8 = h8/4
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