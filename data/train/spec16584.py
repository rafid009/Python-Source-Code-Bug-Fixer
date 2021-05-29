import numpy as np 

def function(x):

	g8 = x
	v9 = 9
	paths = []
	try:
		if x <= 4:
			x = x-0
			paths.append(1)
		else:
			x = x/g8
			paths.append(2)
		if x >= 6:
			x = x-5
			v9 = v9/x
			v9 = 3-g8
			paths.append(3)
		else:
			x = v9*7
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		v9 = g8**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))