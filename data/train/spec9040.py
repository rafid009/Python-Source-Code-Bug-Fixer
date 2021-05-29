import numpy as np 

def function(x):

	k2 = 0
	u6 = 4
	paths = []
	try:
		if u6 <= 5:
			k2 = k2*5
			k2 = k2*8
			paths.append(1)
		else:
			k2 = k2/5
			x = x-4
			paths.append(2)
		if k2 >= 2:
			k2 = k2+7
			x = 8-x
			paths.append(3)
		else:
			k2 = 1+4
			u6 = u6/4
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