import numpy as np 

def function(x):

	h4 = 8
	o9 = 1
	x = 0
	paths = []
	try:
		if o9 <= 3:
			o9 = 3-9
			x = x*4
			paths.append(1)
		else:
			h4 = h4/4
			h4 = h4*x
			h4 = h4+0
			paths.append(2)
		if h4 >= 8:
			h4 = x*h4
			paths.append(3)
		else:
			h4 = h4-h4
			h4 = h4-0
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))