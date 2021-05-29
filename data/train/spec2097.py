import numpy as np 

def function(x):

	i3 = 9
	h5 = 0
	paths = []
	try:
		if i3 < 9:
			x = 1-5
			paths.append(1)
		else:
			h5 = 6+4
			x = x/6
			paths.append(2)
		if h5 <= 5:
			i3 = i3+3
			x = 9/x
			paths.append(3)
		else:
			i3 = 7+h5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))