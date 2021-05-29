import numpy as np 

def function(x):

	o8 = x
	h2 = 5
	paths = []
	try:
		if x <= 0:
			h2 = 6/7
			paths.append(1)
		else:
			x = o8+x
			paths.append(2)
		if x <= 6:
			h2 = h2-8
			o8 = o8-3
			h2 = h2*2
			paths.append(3)
		else:
			h2 = 2*h2
			x = x-o8
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))