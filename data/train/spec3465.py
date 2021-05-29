import numpy as np 

def function(x):

	h7 = 3
	o8 = x
	paths = []
	try:
		if o8 < 6:
			o8 = 4-o8
			h7 = x*h7
			paths.append(1)
		else:
			o8 = o8-6
			o8 = o8*0
			paths.append(2)
		if h7 > 0:
			h7 = h7-5
			o8 = o8-x
			paths.append(3)
		else:
			x = x/o8
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