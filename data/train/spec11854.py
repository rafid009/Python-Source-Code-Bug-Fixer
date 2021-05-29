import numpy as np 

def function(x):

	i4 = x
	u1 = 4
	paths = []
	try:
		if x >= 9:
			i4 = u1*8
			paths.append(1)
		else:
			i4 = 7/i4
			u1 = u1*8
			i4 = x-i4
			paths.append(2)
		if i4 < 8:
			x = 5-x
			u1 = u1/x
			paths.append(3)
		else:
			x = i4-6
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