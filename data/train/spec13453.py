import numpy as np 

def function(x):

	u5 = 5
	n0 = x
	paths = []
	try:
		if u5 < 2:
			x = 0/x
			x = 0/x
			paths.append(1)
		else:
			n0 = n0-0
			x = 5-7
			paths.append(2)
		if u5 >= 4:
			u5 = u5/1
			n0 = 7-x
			u5 = u5/1
			paths.append(3)
		else:
			u5 = n0+2
			n0 = n0/3
			u5 = u5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))