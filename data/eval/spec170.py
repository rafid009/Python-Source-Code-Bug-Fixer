import numpy as np 

def function(x):

	h8 = 2
	o2 = 5
	paths = []
	try:
		if o2 >= 4:
			o2 = o2-4
			h8 = 7-9
			paths.append(1)
		else:
			o2 = 9*o2
			paths.append(2)
		if o2 < 6:
			h8 = h8+9
			o2 = x/o2
			paths.append(3)
		else:
			h8 = 3*h8
			o2 = h8/7
			h8 = 0/h8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))