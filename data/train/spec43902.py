import numpy as np 

def function(x):

	m6 = x
	h4 = x
	paths = []
	try:
		if x > 3:
			m6 = 6+m6
			h4 = h4/h4
			h4 = h4*x
			paths.append(1)
		else:
			h4 = 9*h4
			m6 = 8*2
			paths.append(2)
		if m6 > 0:
			m6 = x/x
			x = x*9
			paths.append(3)
		else:
			h4 = 3-h4
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