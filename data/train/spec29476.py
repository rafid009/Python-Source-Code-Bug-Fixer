import numpy as np 

def function(x):

	k7 = x
	u4 = x
	paths = []
	try:
		if k7 > 5:
			x = x+8
			x = 0-4
			k7 = 0-k7
			paths.append(1)
		else:
			k7 = k7-8
			paths.append(2)
		if k7 < 3:
			x = 3+3
			x = u4*4
			paths.append(3)
		else:
			u4 = 6*u4
			k7 = k7*6
			u4 = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))