import numpy as np 

def function(x):

	h1 = 7
	o2 = x
	x = x
	paths = []
	try:
		if o2 >= 4:
			o2 = o2-h1
			paths.append(1)
		else:
			o2 = o2-h1
			x = o2/9
			h1 = 7+6
			paths.append(2)
		if h1 > 2:
			x = h1+h1
			o2 = 3-6
			paths.append(3)
		else:
			o2 = o2*6
			h1 = 3+h1
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		h1 = o2**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))