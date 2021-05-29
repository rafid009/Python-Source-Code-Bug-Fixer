import numpy as np 

def function(x):

	h8 = x
	o7 = x
	paths = []
	try:
		if o7 > 2:
			x = 1-4
			h8 = 1+4
			o7 = o7*1
			paths.append(1)
		else:
			x = o7*4
			o7 = 2/o7
			x = x/6
			paths.append(2)
		if o7 > 0:
			x = 7/x
			h8 = h8/x
			paths.append(3)
		else:
			x = x+x
			o7 = 2+o7
			o7 = 5*o7
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))