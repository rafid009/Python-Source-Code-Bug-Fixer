import numpy as np 

def function(x):

	n7 = x
	f4 = x
	paths = []
	try:
		if x >= 6:
			x = 2/2
			paths.append(1)
		else:
			x = x+f4
			n7 = n7-6
			paths.append(2)
		if f4 < 2:
			x = f4-4
			f4 = 0-f4
			n7 = 8+n7
			paths.append(3)
		else:
			x = f4+7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))