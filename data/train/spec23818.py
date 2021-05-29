import numpy as np 

def function(x):

	u2 = 6
	n4 = 8
	paths = []
	try:
		if u2 >= 5:
			n4 = n4*0
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x >= 4:
			u2 = 8/4
			x = x+4
			paths.append(3)
		else:
			n4 = x+n4
			u2 = u2*n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		u2 = n4**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))