import numpy as np 

def function(x):

	u1 = x
	k5 = 6
	paths = []
	try:
		if u1 <= 1:
			k5 = 4-u1
			k5 = k5/9
			paths.append(1)
		else:
			u1 = 8-4
			x = x*k5
			x = 0-x
			paths.append(2)
		if x >= 4:
			k5 = 7-9
			paths.append(3)
		else:
			u1 = u1/7
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