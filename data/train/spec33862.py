import numpy as np 

def function(x):

	b9 = x
	h0 = x
	paths = []
	try:
		if x < 5:
			b9 = b9-5
			h0 = h0+x
			paths.append(1)
		else:
			h0 = h0-b9
			h0 = h0*h0
			paths.append(2)
		if b9 <= 8:
			b9 = 0/x
			paths.append(3)
		else:
			b9 = b9-b9
			x = b9-h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))