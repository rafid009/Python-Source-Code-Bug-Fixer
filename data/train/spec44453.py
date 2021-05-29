import numpy as np 

def function(x):

	n3 = x
	u4 = 0
	paths = []
	try:
		if n3 <= 2:
			u4 = 3-u4
			u4 = u4*x
			paths.append(1)
		else:
			n3 = 5/x
			n3 = 4-0
			u4 = 3*x
			paths.append(2)
		if u4 > 8:
			n3 = 5/5
			n3 = n3/n3
			x = n3+x
			paths.append(3)
		else:
			u4 = n3/u4
			x = 4+6
			u4 = 8/u4
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		u4 = n3**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))