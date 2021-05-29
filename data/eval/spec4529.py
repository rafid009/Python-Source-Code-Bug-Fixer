import numpy as np 

def function(x):

	h3 = 9
	u0 = x
	x = x
	paths = []
	try:
		if h3 <= 8:
			x = h3-x
			u0 = u0/7
			paths.append(1)
		else:
			h3 = x-1
			x = 7-x
			x = x*2
			paths.append(2)
		if u0 < 2:
			u0 = u0-2
			paths.append(3)
		else:
			x = 3+8
			u0 = u0/4
			h3 = h3*4
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))