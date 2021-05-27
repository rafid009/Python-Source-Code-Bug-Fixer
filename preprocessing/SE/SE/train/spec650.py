import numpy as np 

def function(x):

	h6 = x
	o2 = 1
	paths = []
	try:
		if x <= 0:
			x = 2*8
			o2 = o2*3
			x = x*x
			paths.append(1)
		else:
			x = x-4
			o2 = o2-8
			paths.append(2)
		if h6 >= 5:
			x = 2+3
			h6 = h6/7
			h6 = h6*0
			paths.append(3)
		else:
			h6 = x-2
			h6 = 6-h6
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		h6 = o2**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))