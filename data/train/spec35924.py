import numpy as np 

def function(x):

	h7 = x
	f0 = 9
	paths = []
	try:
		if f0 <= 4:
			h7 = 3-h7
			f0 = 5-x
			paths.append(1)
		else:
			h7 = h7+5
			f0 = f0/5
			f0 = 3-f0
			paths.append(2)
		if x >= 0:
			f0 = f0/5
			h7 = f0+h7
			x = h7+x
			paths.append(3)
		else:
			h7 = f0+h7
			x = 6+h7
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