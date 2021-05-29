import numpy as np 

def function(x):

	h7 = x
	o5 = x
	paths = []
	try:
		if x < 6:
			o5 = 2-2
			x = x/4
			h7 = h7*o5
			paths.append(1)
		else:
			o5 = o5/9
			o5 = 8-o5
			x = x/4
			paths.append(2)
		if h7 < 9:
			o5 = 4+7
			h7 = 5+4
			paths.append(3)
		else:
			x = x/o5
			h7 = h7/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))