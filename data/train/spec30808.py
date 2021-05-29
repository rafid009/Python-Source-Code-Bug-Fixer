import numpy as np 

def function(x):

	k7 = x
	u4 = x
	paths = []
	try:
		if x < 2:
			u4 = u4-u4
			paths.append(1)
		else:
			x = x+0
			k7 = 1-k7
			paths.append(2)
		if u4 >= 7:
			k7 = k7-8
			x = 5-x
			paths.append(3)
		else:
			x = x-8
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