import numpy as np 

def function(x):

	m8 = 6
	h7 = x
	paths = []
	try:
		if h7 >= 9:
			x = x-0
			paths.append(1)
		else:
			h7 = h7/4
			paths.append(2)
		if x > 2:
			h7 = h7+5
			paths.append(3)
		else:
			x = x+5
			h7 = 0-m8
			x = x*7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		m8 = h7**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))