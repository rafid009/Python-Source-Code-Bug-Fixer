import numpy as np 

def function(x):

	i8 = 3
	h4 = x
	paths = []
	try:
		if i8 < 6:
			x = 9*x
			i8 = i8*4
			paths.append(1)
		else:
			i8 = 4/x
			x = i8*i8
			paths.append(2)
		if h4 <= 9:
			i8 = h4+i8
			i8 = 4/i8
			i8 = 6-3
			paths.append(3)
		else:
			h4 = h4-5
			x = 4-h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		i8 = h4**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))