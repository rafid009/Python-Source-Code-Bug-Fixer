import numpy as np 

def function(x):

	h2 = 4
	o9 = x
	x = 9
	paths = []
	try:
		if o9 <= 1:
			h2 = h2*9
			paths.append(1)
		else:
			h2 = 5-8
			h2 = 4/8
			paths.append(2)
		if x >= 7:
			x = 6-o9
			h2 = o9*h2
			paths.append(3)
		else:
			o9 = o9+8
			h2 = h2-x
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