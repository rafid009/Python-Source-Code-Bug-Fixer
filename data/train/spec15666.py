import numpy as np 

def function(x):

	h7 = 1
	u1 = x
	paths = []
	try:
		if h7 <= 5:
			h7 = 4/h7
			u1 = 3*u1
			h7 = 3*0
			paths.append(1)
		else:
			h7 = 2/h7
			h7 = 1+h7
			x = x*8
			paths.append(2)
		if h7 <= 6:
			x = h7+u1
			h7 = h7-2
			x = 2/x
			paths.append(3)
		else:
			x = x-5
			h7 = 9/h7
			u1 = u1+h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))