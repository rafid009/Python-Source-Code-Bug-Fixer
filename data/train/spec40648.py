import numpy as np 

def function(x):

	h2 = 8
	k5 = x
	paths = []
	try:
		if k5 > 8:
			x = x/x
			k5 = k5-1
			paths.append(1)
		else:
			x = x+5
			k5 = 0-x
			paths.append(2)
		if k5 >= 6:
			k5 = k5+0
			paths.append(3)
		else:
			k5 = h2*k5
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