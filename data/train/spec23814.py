import numpy as np 

def function(x):

	h1 = 7
	o8 = x
	paths = []
	try:
		if h1 <= 3:
			x = x-3
			paths.append(1)
		else:
			x = x/h1
			x = x-0
			paths.append(2)
		if o8 >= 6:
			h1 = o8/o8
			o8 = o8-4
			x = x+0
			paths.append(3)
		else:
			o8 = o8+x
			h1 = 6+4
			h1 = h1+h1
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		h1 = o8**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))