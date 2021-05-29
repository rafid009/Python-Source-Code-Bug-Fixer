import numpy as np 

def function(x):

	k7 = 1
	x4 = 1
	paths = []
	try:
		if k7 >= 2:
			k7 = 4+5
			paths.append(1)
		else:
			x = 1/8
			x4 = x+x4
			paths.append(2)
		if x > 6:
			k7 = k7-x
			k7 = x4*k7
			paths.append(3)
		else:
			k7 = k7-9
			x4 = 5+x4
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x4 = k7**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))