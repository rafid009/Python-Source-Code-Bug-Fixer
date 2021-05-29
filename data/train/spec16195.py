import numpy as np 

def function(x):

	h9 = 9
	m4 = x
	paths = []
	try:
		if m4 < 5:
			h9 = 9-h9
			x = x*h9
			paths.append(1)
		else:
			x = x-6
			x = 9+x
			paths.append(2)
		if m4 <= 5:
			m4 = m4/7
			h9 = 5-x
			x = x*x
			paths.append(3)
		else:
			m4 = m4*8
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))