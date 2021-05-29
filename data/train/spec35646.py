import numpy as np 

def function(x):

	h0 = 5
	v7 = 2
	paths = []
	try:
		if x >= 4:
			v7 = v7*0
			paths.append(1)
		else:
			x = x/6
			h0 = h0-h0
			x = x+5
			paths.append(2)
		if x >= 2:
			x = x+0
			v7 = v7*3
			paths.append(3)
		else:
			h0 = h0-9
			v7 = v7-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))