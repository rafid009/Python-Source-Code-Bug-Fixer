import numpy as np 

def function(x):

	k5 = 1
	a8 = x
	paths = []
	try:
		if x < 8:
			x = 2+8
			paths.append(1)
		else:
			k5 = 6+8
			k5 = k5*k5
			paths.append(2)
		if x <= 9:
			k5 = 9+k5
			paths.append(3)
		else:
			k5 = 9-x
			x = 0+x
			k5 = 0/k5
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))