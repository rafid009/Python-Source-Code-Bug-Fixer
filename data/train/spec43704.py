import numpy as np 

def function(x):

	h7 = 2
	f4 = x
	paths = []
	try:
		if h7 >= 4:
			x = 2+x
			f4 = 5+h7
			paths.append(1)
		else:
			f4 = 9-4
			x = 4-x
			paths.append(2)
		if h7 <= 9:
			h7 = 4-f4
			x = 7*3
			x = h7-x
			paths.append(3)
		else:
			h7 = h7/h7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))