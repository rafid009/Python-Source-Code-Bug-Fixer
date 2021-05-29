import numpy as np 

def function(x):

	h4 = 2
	f2 = 8
	x = x
	paths = []
	try:
		if h4 > 3:
			f2 = f2/6
			paths.append(1)
		else:
			f2 = 7+f2
			h4 = h4-f2
			f2 = f2*8
			paths.append(2)
		if x >= 7:
			f2 = h4+f2
			paths.append(3)
		else:
			h4 = 3+h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))