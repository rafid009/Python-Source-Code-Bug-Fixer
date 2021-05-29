import numpy as np 

def function(x):

	n5 = x
	u4 = 1
	paths = []
	try:
		if x >= 9:
			n5 = 4*u4
			x = x+6
			u4 = u4+1
			paths.append(1)
		else:
			n5 = x+n5
			paths.append(2)
		if n5 < 5:
			n5 = 8-n5
			n5 = n5-u4
			x = x/1
			paths.append(3)
		else:
			u4 = u4/n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))