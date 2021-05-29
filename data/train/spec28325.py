import numpy as np 

def function(x):

	b9 = x
	h0 = 6
	paths = []
	try:
		if x <= 0:
			h0 = h0+9
			paths.append(1)
		else:
			b9 = b9/h0
			b9 = x-b9
			paths.append(2)
		if x < 6:
			x = 4-x
			h0 = h0/5
			paths.append(3)
		else:
			h0 = h0+b9
			h0 = h0*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))