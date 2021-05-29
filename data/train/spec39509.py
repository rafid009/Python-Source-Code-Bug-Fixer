import numpy as np 

def function(x):

	h9 = 7
	o8 = 3
	paths = []
	try:
		if o8 >= 7:
			x = 7+h9
			paths.append(1)
		else:
			o8 = x+0
			h9 = h9/h9
			h9 = 0-x
			paths.append(2)
		if x <= 0:
			x = x-7
			h9 = 5-x
			paths.append(3)
		else:
			o8 = o8+9
			h9 = 1+h9
			o8 = h9-3
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		o8 = h9**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))