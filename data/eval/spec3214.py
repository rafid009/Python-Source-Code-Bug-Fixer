import numpy as np 

def function(x):

	h0 = x
	m2 = x
	x = 2
	paths = []
	try:
		if m2 > 1:
			h0 = h0+5
			paths.append(1)
		else:
			h0 = h0+h0
			x = h0+4
			paths.append(2)
		if x < 2:
			x = 0*x
			m2 = m2-4
			paths.append(3)
		else:
			m2 = m2*5
			x = x+x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		h0 = m2**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))