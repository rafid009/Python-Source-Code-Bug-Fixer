import numpy as np 

def function(x):

	h2 = x
	f2 = 1
	paths = []
	try:
		if h2 > 6:
			h2 = 6-h2
			h2 = 3-0
			f2 = f2+8
			paths.append(1)
		else:
			f2 = 8*h2
			paths.append(2)
		if h2 >= 3:
			f2 = 7+f2
			h2 = f2+h2
			h2 = h2+9
			paths.append(3)
		else:
			h2 = h2-5
			x = f2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))