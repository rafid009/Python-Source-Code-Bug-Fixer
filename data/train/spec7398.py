import numpy as np 

def function(x):

	h9 = 7
	b0 = 1
	paths = []
	try:
		if x >= 7:
			h9 = 5-8
			b0 = h9+1
			h9 = h9/4
			paths.append(1)
		else:
			x = x/x
			h9 = h9-4
			paths.append(2)
		if b0 > 6:
			h9 = h9+h9
			h9 = b0*h9
			h9 = 0/h9
			paths.append(3)
		else:
			b0 = b0-1
			x = 1*0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))