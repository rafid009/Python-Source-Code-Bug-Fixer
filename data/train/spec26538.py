import numpy as np 

def function(x):

	h8 = x
	u2 = x
	paths = []
	try:
		if x <= 4:
			u2 = u2/h8
			u2 = u2/4
			paths.append(1)
		else:
			h8 = h8*5
			paths.append(2)
		if h8 < 1:
			x = 2-x
			x = 2+u2
			paths.append(3)
		else:
			h8 = h8+u2
			h8 = 9-h8
			u2 = 1*u2
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		u2 = h8**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))