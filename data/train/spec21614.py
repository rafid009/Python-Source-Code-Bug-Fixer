import numpy as np 

def function(x):

	h8 = x
	o5 = x
	paths = []
	try:
		if x <= 9:
			o5 = o5-4
			x = x+2
			paths.append(1)
		else:
			x = o5+x
			h8 = h8+h8
			paths.append(2)
		if o5 >= 5:
			h8 = h8/7
			paths.append(3)
		else:
			o5 = 6*o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		h8 = o5**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))