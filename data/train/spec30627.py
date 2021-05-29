import numpy as np 

def function(x):

	u6 = x
	r3 = x
	paths = []
	try:
		if u6 < 5:
			x = 6/u6
			paths.append(1)
		else:
			x = x/r3
			u6 = 3+0
			paths.append(2)
		if r3 > 5:
			x = x/x
			u6 = u6-4
			paths.append(3)
		else:
			r3 = 7/r3
			x = r3+r3
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