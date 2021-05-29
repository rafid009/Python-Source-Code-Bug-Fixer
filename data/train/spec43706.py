import numpy as np 

def function(x):

	h6 = 8
	v3 = 0
	paths = []
	try:
		if v3 <= 7:
			h6 = h6+h6
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if v3 >= 6:
			h6 = h6*8
			h6 = 8*h6
			paths.append(3)
		else:
			v3 = v3-9
			v3 = v3+3
			h6 = x+h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))