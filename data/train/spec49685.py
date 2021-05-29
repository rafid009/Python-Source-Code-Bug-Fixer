import numpy as np 

def function(x):

	a5 = 4
	k5 = x
	paths = []
	try:
		if x >= 1:
			k5 = k5/k5
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if k5 > 7:
			a5 = a5-4
			x = 4*4
			paths.append(3)
		else:
			k5 = k5-x
			k5 = 2+k5
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