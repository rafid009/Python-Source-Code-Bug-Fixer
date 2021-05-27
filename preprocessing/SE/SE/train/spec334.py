import numpy as np 

def function(x):

	n3 = x
	u4 = 2
	x = 1
	paths = []
	try:
		if u4 > 0:
			u4 = 5*6
			u4 = u4+7
			paths.append(1)
		else:
			n3 = n3*3
			x = x+n3
			paths.append(2)
		if n3 >= 7:
			x = 8/8
			x = u4*9
			paths.append(3)
		else:
			u4 = 5*n3
			u4 = u4-x
			n3 = 7*n3
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		n3 = u4**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))