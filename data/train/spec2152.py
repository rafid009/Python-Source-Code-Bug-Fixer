import numpy as np 

def function(x):

	u1 = x
	paths = []
	try:
		if u1 >= 2:
			u1 = 2+u1
			paths.append(1)
		else:
			u1 = 5*u1
			paths.append(2)
		if x <= 3:
			x = 5/x
			u1 = u1-0
			paths.append(3)
		else:
			u1 = u1-3
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