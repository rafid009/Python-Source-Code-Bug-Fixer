import numpy as np 

def function(x):

	f1 = 4
	h0 = 4
	paths = []
	try:
		if x <= 4:
			h0 = h0*4
			h0 = 6+h0
			paths.append(1)
		else:
			h0 = h0-2
			f1 = 5*f1
			paths.append(2)
		if f1 > 2:
			f1 = f1/x
			h0 = f1+5
			h0 = 3-7
			paths.append(3)
		else:
			h0 = h0-1
			f1 = 4+f1
			h0 = h0*3
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		h0 = f1**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))