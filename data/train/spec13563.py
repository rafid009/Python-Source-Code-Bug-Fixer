import numpy as np 

def function(x):

	x8 = 8
	k7 = 4
	paths = []
	try:
		if k7 <= 1:
			x = 5/k7
			x8 = x8*6
			k7 = k7-9
			paths.append(1)
		else:
			x8 = x8+x8
			k7 = k7*6
			x = 8+x
			paths.append(2)
		if x8 > 6:
			x = 3-x
			paths.append(3)
		else:
			x = 8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))