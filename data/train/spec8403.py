import numpy as np 

def function(x):

	h5 = x
	m9 = x
	paths = []
	try:
		if h5 >= 0:
			h5 = 5-8
			m9 = m9/9
			paths.append(1)
		else:
			h5 = 5-h5
			h5 = 9*h5
			paths.append(2)
		if h5 >= 0:
			x = 7*h5
			h5 = h5*6
			paths.append(3)
		else:
			m9 = 6+m9
			x = 2-x
			x = h5*x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))