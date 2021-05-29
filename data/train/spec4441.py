import numpy as np 

def function(x):

	u4 = 8
	n4 = x
	paths = []
	try:
		if n4 < 0:
			n4 = n4+8
			paths.append(1)
		else:
			x = x+6
			n4 = x/2
			paths.append(2)
		if u4 <= 8:
			u4 = u4+3
			u4 = u4*n4
			paths.append(3)
		else:
			n4 = u4+2
			n4 = n4+5
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