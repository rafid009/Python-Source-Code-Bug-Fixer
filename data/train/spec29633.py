import numpy as np 

def function(x):

	h7 = 4
	e0 = x
	paths = []
	try:
		if x < 7:
			h7 = e0/h7
			paths.append(1)
		else:
			e0 = e0+x
			paths.append(2)
		if e0 < 8:
			h7 = h7*h7
			h7 = h7*h7
			x = x/8
			paths.append(3)
		else:
			h7 = 3*h7
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))