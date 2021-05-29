import numpy as np 

def function(x):

	u4 = 6
	u1 = x
	paths = []
	try:
		if x > 5:
			u4 = u4*6
			x = x/x
			x = x/8
			paths.append(1)
		else:
			u1 = u1+4
			u4 = u4+5
			u1 = 7/u1
			paths.append(2)
		if u4 > 4:
			x = x-3
			paths.append(3)
		else:
			x = x*8
			u4 = u4/u4
			u4 = u1-u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))