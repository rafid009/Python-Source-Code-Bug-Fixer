import numpy as np 

def function(x):

	h6 = 0
	u1 = x
	x = 4
	paths = []
	try:
		if u1 < 2:
			h6 = h6+x
			h6 = h6-7
			u1 = u1*u1
			paths.append(1)
		else:
			u1 = 5*u1
			paths.append(2)
		if h6 >= 4:
			x = h6/x
			x = x-3
			paths.append(3)
		else:
			x = x+u1
			u1 = u1+1
			u1 = h6/6
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))