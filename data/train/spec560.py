import numpy as np 

def function(x):

	v6 = 6
	u4 = 6
	paths = []
	try:
		if u4 >= 9:
			u4 = u4+u4
			v6 = v6-1
			paths.append(1)
		else:
			u4 = x-v6
			u4 = 7-u4
			v6 = v6-v6
			paths.append(2)
		if v6 >= 9:
			v6 = 5+x
			x = v6*x
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))