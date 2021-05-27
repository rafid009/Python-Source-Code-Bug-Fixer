import numpy as np 

def function(x):

	u6 = x
	n4 = x
	paths = []
	try:
		if n4 > 9:
			n4 = 4/n4
			u6 = 5/x
			paths.append(1)
		else:
			n4 = n4+x
			u6 = 6+1
			u6 = u6-3
			paths.append(2)
		if n4 > 9:
			u6 = 1*u6
			paths.append(3)
		else:
			n4 = n4+4
			u6 = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))