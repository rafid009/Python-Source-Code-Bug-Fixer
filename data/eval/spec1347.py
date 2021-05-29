import numpy as np 

def function(x):

	u5 = x
	k2 = 9
	paths = []
	try:
		if u5 <= 2:
			k2 = 3+2
			paths.append(1)
		else:
			u5 = u5*8
			u5 = 1-u5
			paths.append(2)
		if k2 < 2:
			u5 = 2+u5
			k2 = k2/4
			paths.append(3)
		else:
			x = u5+2
			u5 = k2-u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))