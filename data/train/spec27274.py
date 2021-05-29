import numpy as np 

def function(x):

	f6 = x
	u1 = 8
	x = 6
	paths = []
	try:
		if x >= 3:
			u1 = 9-0
			x = 3-x
			f6 = f6/7
			paths.append(1)
		else:
			x = f6*x
			f6 = u1-f6
			paths.append(2)
		if f6 < 5:
			x = 1-x
			x = x/f6
			paths.append(3)
		else:
			u1 = 9*u1
			u1 = 4/x
			f6 = f6/f6
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