import numpy as np 

def function(x):

	m1 = x
	h0 = x
	paths = []
	try:
		if x < 9:
			h0 = 5*h0
			paths.append(1)
		else:
			h0 = h0+0
			paths.append(2)
		if m1 > 6:
			x = 7-x
			x = m1*m1
			m1 = 2/x
			paths.append(3)
		else:
			h0 = 5/2
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