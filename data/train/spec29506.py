import numpy as np 

def function(x):

	v4 = 8
	u1 = x
	paths = []
	try:
		if x <= 8:
			u1 = 4+u1
			paths.append(1)
		else:
			v4 = v4/4
			v4 = 6-v4
			u1 = 0-u1
			paths.append(2)
		if v4 >= 5:
			u1 = 9-v4
			paths.append(3)
		else:
			v4 = 2/v4
			v4 = x*1
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