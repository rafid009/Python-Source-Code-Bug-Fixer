import numpy as np 

def function(x):

	r5 = x
	h7 = 4
	paths = []
	try:
		if h7 > 4:
			h7 = x+8
			r5 = r5-9
			paths.append(1)
		else:
			x = x/9
			r5 = r5*3
			paths.append(2)
		if r5 < 7:
			h7 = h7*r5
			r5 = 1*r5
			paths.append(3)
		else:
			h7 = 8+h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))