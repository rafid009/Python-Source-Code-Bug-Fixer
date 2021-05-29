import numpy as np 

def function(x):

	i9 = x
	h0 = x
	x = 5
	paths = []
	try:
		if i9 <= 4:
			i9 = 9+i9
			paths.append(1)
		else:
			h0 = h0-h0
			paths.append(2)
		if x <= 8:
			x = 3+6
			paths.append(3)
		else:
			h0 = 2+x
			i9 = i9*4
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		i9 = h0**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))