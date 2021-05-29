import numpy as np 

def function(x):

	h7 = 6
	i4 = 6
	paths = []
	try:
		if i4 >= 8:
			x = 7*x
			x = 1-4
			i4 = i4/i4
			paths.append(1)
		else:
			h7 = i4-h7
			i4 = x-i4
			paths.append(2)
		if x <= 7:
			i4 = h7-i4
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))