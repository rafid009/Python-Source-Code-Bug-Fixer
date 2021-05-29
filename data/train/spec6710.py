import numpy as np 

def function(x):

	a0 = 4
	h3 = 3
	x = x
	paths = []
	try:
		if x < 0:
			a0 = h3*x
			x = x-8
			a0 = a0+8
			paths.append(1)
		else:
			h3 = 9*1
			paths.append(2)
		if x >= 4:
			h3 = h3-2
			h3 = h3-5
			paths.append(3)
		else:
			h3 = h3+x
			x = h3*2
			h3 = h3-9
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		h3 = a0**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))