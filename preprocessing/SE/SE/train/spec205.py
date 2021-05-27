import numpy as np 

def function(x):

	h8 = 1
	m1 = x
	paths = []
	try:
		if h8 < 5:
			m1 = 7+m1
			m1 = 4*2
			h8 = 9*h8
			paths.append(1)
		else:
			m1 = m1+0
			paths.append(2)
		if h8 >= 7:
			h8 = h8/x
			h8 = 0-h8
			paths.append(3)
		else:
			x = 1+4
			h8 = 0+h8
			m1 = 9-m1
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))