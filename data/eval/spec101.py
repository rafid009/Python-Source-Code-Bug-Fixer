import numpy as np 

def function(x):

	h2 = 0
	m5 = 1
	paths = []
	try:
		if m5 >= 6:
			m5 = h2-m5
			paths.append(1)
		else:
			h2 = h2*6
			paths.append(2)
		if m5 <= 3:
			m5 = m5*8
			h2 = 7+h2
			paths.append(3)
		else:
			x = x-4
			x = m5/m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))