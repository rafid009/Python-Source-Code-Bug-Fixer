import numpy as np 

def function(x):

	r3 = 1
	h7 = 6
	paths = []
	try:
		if h7 < 4:
			r3 = 1+x
			paths.append(1)
		else:
			r3 = 4*6
			x = x+2
			x = x+x
			paths.append(2)
		if h7 <= 9:
			x = x*h7
			x = x+x
			h7 = x/h7
			paths.append(3)
		else:
			h7 = r3/h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))