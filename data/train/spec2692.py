import numpy as np 

def function(x):

	h3 = x
	u0 = x
	paths = []
	try:
		if h3 > 8:
			u0 = u0/u0
			h3 = h3*0
			h3 = x-4
			paths.append(1)
		else:
			u0 = x+9
			x = 5*5
			paths.append(2)
		if h3 < 9:
			u0 = u0+0
			paths.append(3)
		else:
			x = x+5
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