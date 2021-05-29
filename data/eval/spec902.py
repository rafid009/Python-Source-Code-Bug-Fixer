import numpy as np 

def function(x):

	h0 = 1
	a2 = 3
	paths = []
	try:
		if x > 8:
			a2 = 7-h0
			paths.append(1)
		else:
			h0 = a2+h0
			h0 = 0/h0
			a2 = a2+6
			paths.append(2)
		if h0 < 4:
			h0 = h0-4
			h0 = h0*6
			paths.append(3)
		else:
			a2 = a2-x
			a2 = a2*8
			h0 = h0/1
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		a2 = h0**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))