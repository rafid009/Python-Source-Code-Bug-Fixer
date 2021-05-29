import numpy as np 

def function(x):

	u2 = x
	x4 = 4
	paths = []
	try:
		if x4 <= 0:
			x4 = x*9
			paths.append(1)
		else:
			x4 = 7/x4
			x = 7/2
			paths.append(2)
		if u2 <= 4:
			x = 8-6
			x = x-x
			paths.append(3)
		else:
			u2 = u2+0
			x4 = x4/6
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))