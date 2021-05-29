import numpy as np 

def function(x):

	h0 = 0
	u5 = 4
	paths = []
	try:
		if u5 >= 2:
			h0 = 9*h0
			paths.append(1)
		else:
			u5 = u5*h0
			x = 2/x
			x = 5+6
			paths.append(2)
		if x > 0:
			x = x+0
			u5 = 7-u5
			x = x/1
			paths.append(3)
		else:
			x = x-7
			u5 = u5*3
			h0 = u5*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))