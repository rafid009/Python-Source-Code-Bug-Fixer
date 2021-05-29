import numpy as np 

def function(x):

	h8 = x
	f8 = 5
	paths = []
	try:
		if f8 < 2:
			h8 = 0+h8
			paths.append(1)
		else:
			f8 = f8-7
			h8 = f8+h8
			f8 = f8-5
			paths.append(2)
		if h8 > 7:
			x = 9+h8
			h8 = x+h8
			x = f8+1
			paths.append(3)
		else:
			h8 = 6-h8
			h8 = h8/6
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))