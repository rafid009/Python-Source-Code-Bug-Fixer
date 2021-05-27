import numpy as np 

def function(x):

	h1 = x
	f7 = 6
	paths = []
	try:
		if x <= 4:
			h1 = h1*4
			x = h1/x
			paths.append(1)
		else:
			f7 = h1/2
			x = 4+8
			paths.append(2)
		if f7 > 9:
			h1 = h1-f7
			f7 = f7/h1
			f7 = h1/f7
			paths.append(3)
		else:
			h1 = h1/x
			f7 = 6+x
			x = x-f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))