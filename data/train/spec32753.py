import numpy as np 

def function(x):

	r1 = x
	u4 = 9
	paths = []
	try:
		if r1 > 6:
			x = 9+x
			u4 = 5/u4
			x = 7/x
			paths.append(1)
		else:
			r1 = u4-4
			paths.append(2)
		if u4 > 8:
			u4 = u4/u4
			paths.append(3)
		else:
			x = r1+u4
			u4 = u4+r1
			x = 6-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))