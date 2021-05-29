import numpy as np 

def function(x):

	u6 = x
	y1 = x
	paths = []
	try:
		if x < 2:
			x = 7/3
			paths.append(1)
		else:
			x = x*y1
			paths.append(2)
		if u6 >= 2:
			x = 7*8
			paths.append(3)
		else:
			x = x-2
			x = 2-u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))