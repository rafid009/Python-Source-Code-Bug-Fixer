import numpy as np 

def function(x):

	o9 = x
	h7 = 0
	paths = []
	try:
		if o9 <= 3:
			h7 = 1+4
			o9 = x*2
			h7 = o9-h7
			paths.append(1)
		else:
			h7 = x+x
			o9 = h7-8
			paths.append(2)
		if h7 < 5:
			o9 = o9-5
			paths.append(3)
		else:
			x = 7+2
			h7 = 9/h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))