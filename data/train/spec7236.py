import numpy as np 

def function(x):

	w4 = 9
	m0 = x
	paths = []
	try:
		if m0 >= 7:
			m0 = w4/6
			m0 = x/m0
			paths.append(1)
		else:
			m0 = m0-9
			w4 = w4+8
			paths.append(2)
		if x <= 7:
			x = 7-5
			m0 = m0-3
			x = x/2
			paths.append(3)
		else:
			x = 4-5
			w4 = w4/8
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