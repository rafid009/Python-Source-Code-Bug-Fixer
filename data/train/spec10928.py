import numpy as np 

def function(x):

	q8 = 9
	k0 = x
	paths = []
	try:
		if k0 > 3:
			q8 = 3*5
			q8 = q8-2
			paths.append(1)
		else:
			k0 = k0+7
			k0 = 3/3
			paths.append(2)
		if k0 >= 6:
			q8 = k0-q8
			k0 = x+k0
			paths.append(3)
		else:
			q8 = q8-6
			q8 = 1/x
			k0 = 0+k0
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		k0 = q8**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))