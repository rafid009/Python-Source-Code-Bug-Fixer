import numpy as np 

def function(x):

	m4 = x
	h8 = x
	paths = []
	try:
		if x > 3:
			h8 = h8+0
			paths.append(1)
		else:
			h8 = 7*h8
			paths.append(2)
		if m4 <= 4:
			x = x/3
			m4 = m4/3
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))