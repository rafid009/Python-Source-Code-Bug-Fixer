import numpy as np 

def function(x):

	h6 = x
	o8 = x
	paths = []
	try:
		if o8 < 1:
			o8 = x+1
			o8 = 1*2
			o8 = 8/o8
			paths.append(1)
		else:
			h6 = h6-2
			h6 = h6/6
			paths.append(2)
		if h6 >= 7:
			o8 = 3-o8
			paths.append(3)
		else:
			x = x/x
			x = x+0
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))