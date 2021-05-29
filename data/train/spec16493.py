import numpy as np 

def function(x):

	o9 = 5
	h7 = 9
	x = 7
	paths = []
	try:
		if o9 <= 1:
			o9 = o9/5
			paths.append(1)
		else:
			o9 = 6/2
			o9 = o9-4
			x = o9-7
			paths.append(2)
		if x >= 5:
			h7 = o9+2
			h7 = h7+3
			o9 = 2/o9
			paths.append(3)
		else:
			x = 4+x
			h7 = h7-2
			h7 = 5-h7
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))