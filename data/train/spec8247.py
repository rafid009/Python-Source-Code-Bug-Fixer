import numpy as np 

def function(x):

	m1 = 4
	h2 = 4
	paths = []
	try:
		if m1 > 6:
			x = m1+0
			h2 = m1+h2
			h2 = 5/x
			paths.append(1)
		else:
			m1 = 6+m1
			paths.append(2)
		if x >= 6:
			h2 = 7*m1
			m1 = m1+6
			h2 = h2+1
			paths.append(3)
		else:
			h2 = h2+4
			x = x/4
			h2 = 1-h2
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