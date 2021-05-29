import numpy as np 

def function(x):

	k5 = 4
	n6 = x
	paths = []
	try:
		if k5 > 3:
			n6 = 7/n6
			k5 = 4+k5
			paths.append(1)
		else:
			x = k5-n6
			paths.append(2)
		if k5 > 7:
			k5 = k5+n6
			paths.append(3)
		else:
			k5 = 9/k5
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