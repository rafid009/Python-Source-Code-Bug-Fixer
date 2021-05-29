import numpy as np 

def function(x):

	h5 = x
	m2 = 4
	paths = []
	try:
		if x > 3:
			x = 0-x
			m2 = 0*5
			paths.append(1)
		else:
			m2 = x-7
			x = 6/x
			paths.append(2)
		if h5 >= 6:
			m2 = m2/1
			paths.append(3)
		else:
			x = x/x
			x = h5+x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))