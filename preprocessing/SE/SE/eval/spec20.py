import numpy as np 

def function(x):

	m7 = 6
	h0 = x
	paths = []
	try:
		if m7 > 0:
			x = x+9
			h0 = 3-4
			paths.append(1)
		else:
			h0 = h0*m7
			x = x-9
			paths.append(2)
		if x >= 7:
			m7 = m7/h0
			paths.append(3)
		else:
			m7 = m7*8
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))