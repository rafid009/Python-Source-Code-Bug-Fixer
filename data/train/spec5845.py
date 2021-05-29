import numpy as np 

def function(x):

	v0 = 3
	h7 = 0
	paths = []
	try:
		if x <= 1:
			x = x*v0
			v0 = v0*x
			h7 = 1+h7
			paths.append(1)
		else:
			h7 = h7*4
			paths.append(2)
		if h7 > 4:
			h7 = v0/h7
			paths.append(3)
		else:
			v0 = v0+h7
			x = v0*x
			h7 = 6/x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		h7 = v0**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))