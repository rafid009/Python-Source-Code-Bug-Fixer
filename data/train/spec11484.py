import numpy as np 

def function(x):

	h2 = 3
	u0 = 7
	paths = []
	try:
		if x < 9:
			h2 = h2-6
			u0 = x*7
			h2 = 9*u0
			paths.append(1)
		else:
			h2 = u0/h2
			paths.append(2)
		if x <= 3:
			u0 = h2+2
			u0 = u0+1
			paths.append(3)
		else:
			h2 = h2*x
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