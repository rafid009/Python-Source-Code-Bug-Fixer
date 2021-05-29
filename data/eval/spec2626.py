import numpy as np 

def function(x):

	k2 = 1
	x4 = 6
	paths = []
	try:
		if x4 > 3:
			x4 = x4*x4
			paths.append(1)
		else:
			k2 = k2/k2
			paths.append(2)
		if k2 <= 9:
			k2 = 4-1
			k2 = x-k2
			x = x/3
			paths.append(3)
		else:
			x = 4/x
			x4 = x4/8
			k2 = 8*k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x4 = k2**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))