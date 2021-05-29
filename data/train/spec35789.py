import numpy as np 

def function(x):

	k7 = 8
	x3 = x
	paths = []
	try:
		if x >= 2:
			x3 = x3-0
			k7 = k7-2
			x = 9*1
			paths.append(1)
		else:
			x = 5/4
			k7 = k7*k7
			paths.append(2)
		if x3 >= 9:
			k7 = k7-k7
			paths.append(3)
		else:
			x3 = x3-2
			x3 = x3/1
			x = k7*5
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))