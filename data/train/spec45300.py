import numpy as np 

def function(x):

	x8 = x
	k7 = 7
	paths = []
	try:
		if x8 >= 7:
			k7 = k7-k7
			paths.append(1)
		else:
			x8 = 0+x8
			paths.append(2)
		if x > 7:
			k7 = 8*5
			paths.append(3)
		else:
			x8 = 5-8
			x = 5+6
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))