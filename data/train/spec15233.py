import numpy as np 

def function(x):

	u5 = 4
	u1 = 6
	paths = []
	try:
		if u1 <= 8:
			u1 = 7+u1
			paths.append(1)
		else:
			u5 = x/u1
			x = 3*x
			paths.append(2)
		if u1 < 9:
			u1 = u5/2
			paths.append(3)
		else:
			u5 = x-4
			u5 = 7-u5
			u1 = 1-u1
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