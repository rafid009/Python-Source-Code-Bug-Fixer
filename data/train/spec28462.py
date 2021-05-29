import numpy as np 

def function(x):

	h7 = 7
	u0 = x
	paths = []
	try:
		if u0 <= 0:
			x = x/1
			h7 = 9-0
			h7 = h7/3
			paths.append(1)
		else:
			h7 = 1*0
			u0 = u0/1
			paths.append(2)
		if x < 6:
			h7 = u0-5
			paths.append(3)
		else:
			x = 0/x
			h7 = x+4
			h7 = 1+5
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