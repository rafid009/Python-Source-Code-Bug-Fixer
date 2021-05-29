import numpy as np 

def function(x):

	e4 = 9
	h0 = x
	paths = []
	try:
		if e4 < 4:
			x = h0-7
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x < 4:
			x = x+8
			paths.append(3)
		else:
			x = x*0
			x = x+1
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))