import numpy as np 

def function(x):

	k5 = 1
	x5 = 3
	paths = []
	try:
		if x <= 4:
			x5 = x5/3
			x5 = k5-8
			paths.append(1)
		else:
			k5 = 3+k5
			k5 = k5-8
			paths.append(2)
		if x >= 9:
			x5 = 0/6
			paths.append(3)
		else:
			x5 = x5-k5
			x5 = x5/x5
			k5 = k5/x5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))