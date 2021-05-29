import numpy as np 

def function(x):

	d7 = x
	u6 = 1
	paths = []
	try:
		if d7 >= 3:
			d7 = 3+d7
			paths.append(1)
		else:
			x = x/5
			d7 = d7-1
			paths.append(2)
		if d7 < 9:
			x = x/5
			paths.append(3)
		else:
			u6 = 0+d7
			u6 = 2-u6
			u6 = u6-4
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