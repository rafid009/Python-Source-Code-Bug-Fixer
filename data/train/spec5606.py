import numpy as np 

def function(x):

	h8 = x
	r3 = 0
	paths = []
	try:
		if x <= 2:
			h8 = h8-9
			h8 = x-3
			x = x+3
			paths.append(1)
		else:
			h8 = x/6
			paths.append(2)
		if x <= 5:
			x = x*5
			x = x/6
			paths.append(3)
		else:
			r3 = 6*r3
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