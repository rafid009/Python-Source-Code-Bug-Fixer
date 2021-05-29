import numpy as np 

def function(x):

	h7 = 5
	m3 = 1
	paths = []
	try:
		if x > 4:
			x = 1*x
			m3 = m3+x
			paths.append(1)
		else:
			h7 = h7-2
			paths.append(2)
		if m3 >= 0:
			h7 = h7-m3
			h7 = 5+h7
			h7 = 7/h7
			paths.append(3)
		else:
			m3 = 9*h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))