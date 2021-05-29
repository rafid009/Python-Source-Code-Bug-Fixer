import numpy as np 

def function(x):

	h1 = 7
	u1 = 7
	x = x
	paths = []
	try:
		if x >= 1:
			h1 = h1*5
			x = u1*u1
			x = x/1
			paths.append(1)
		else:
			x = x*9
			u1 = 3-u1
			x = 4-h1
			paths.append(2)
		if x > 2:
			x = 5*x
			x = u1/x
			u1 = 4/u1
			paths.append(3)
		else:
			u1 = 2*u1
			u1 = u1*8
			x = x+u1
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