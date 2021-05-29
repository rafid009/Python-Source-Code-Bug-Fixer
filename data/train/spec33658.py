import numpy as np 

def function(x):

	m6 = 2
	h7 = x
	paths = []
	try:
		if h7 < 9:
			x = 9/x
			x = h7+3
			paths.append(1)
		else:
			m6 = 5+m6
			h7 = h7/3
			x = 5*x
			paths.append(2)
		if m6 >= 1:
			x = x+x
			paths.append(3)
		else:
			h7 = h7+m6
			h7 = h7*1
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))