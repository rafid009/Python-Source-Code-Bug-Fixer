import numpy as np 

def function(x):

	k0 = 9
	k5 = x
	paths = []
	try:
		if k0 > 8:
			k0 = k0/k5
			x = 3*x
			k5 = k5-8
			paths.append(1)
		else:
			k5 = 2+2
			paths.append(2)
		if k0 <= 5:
			k5 = 2+k5
			paths.append(3)
		else:
			k5 = k5-6
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))