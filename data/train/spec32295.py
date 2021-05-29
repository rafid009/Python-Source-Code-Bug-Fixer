import numpy as np 

def function(x):

	x3 = x
	k2 = 7
	paths = []
	try:
		if k2 >= 0:
			x3 = x3+2
			x3 = 9/9
			x3 = x-k2
			paths.append(1)
		else:
			x = x/x3
			k2 = 0-x
			paths.append(2)
		if k2 <= 9:
			x3 = x3+6
			k2 = k2*5
			k2 = x3-9
			paths.append(3)
		else:
			x3 = x3/3
			x3 = 7/1
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))