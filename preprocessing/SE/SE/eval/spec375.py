import numpy as np 

def function(x):

	h7 = 2
	e9 = x
	x = 5
	paths = []
	try:
		if x <= 0:
			e9 = e9+3
			e9 = e9/h7
			h7 = h7+4
			paths.append(1)
		else:
			e9 = 4/e9
			paths.append(2)
		if h7 < 1:
			x = 9/7
			paths.append(3)
		else:
			h7 = 4+h7
			x = x/6
			h7 = 2-e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		h7 = e9**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))