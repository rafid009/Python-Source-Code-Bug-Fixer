import numpy as np 

def function(x):

	u4 = 5
	n6 = 3
	paths = []
	try:
		if u4 >= 4:
			x = x*n6
			paths.append(1)
		else:
			n6 = 6+n6
			paths.append(2)
		if n6 < 0:
			u4 = u4*2
			x = 5+0
			paths.append(3)
		else:
			u4 = x-u4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		n6 = u4**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))