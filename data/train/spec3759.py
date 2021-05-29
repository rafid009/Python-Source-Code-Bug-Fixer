import numpy as np 

def function(x):

	b7 = x
	h7 = x
	paths = []
	try:
		if b7 < 3:
			b7 = b7*0
			h7 = h7+x
			h7 = 5/h7
			paths.append(1)
		else:
			b7 = b7-2
			paths.append(2)
		if h7 > 2:
			x = 9-x
			paths.append(3)
		else:
			h7 = h7*6
			b7 = b7*4
			b7 = h7+x
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