import numpy as np 

def function(x):

	u4 = x
	u2 = 8
	paths = []
	try:
		if u4 > 5:
			u4 = u2*x
			paths.append(1)
		else:
			u4 = 1*5
			u4 = u4*6
			paths.append(2)
		if u2 > 3:
			u2 = u2-9
			u2 = 1+x
			u2 = u2-8
			paths.append(3)
		else:
			x = x+4
			u4 = 1/u4
			x = u2-u4
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