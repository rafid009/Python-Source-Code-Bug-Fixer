import numpy as np 

def function(x):

	h3 = 8
	v0 = x
	paths = []
	try:
		if v0 <= 8:
			h3 = 2-h3
			h3 = h3*h3
			paths.append(1)
		else:
			v0 = v0/3
			x = 9*h3
			v0 = v0*v0
			paths.append(2)
		if x >= 4:
			h3 = h3+5
			x = x*v0
			paths.append(3)
		else:
			h3 = h3-v0
			v0 = 1-v0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		h3 = v0**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))