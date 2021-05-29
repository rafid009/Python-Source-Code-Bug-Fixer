import numpy as np 

def function(x):

	x0 = x
	k9 = x
	paths = []
	try:
		if k9 >= 8:
			x0 = 6-7
			paths.append(1)
		else:
			x0 = x0-2
			paths.append(2)
		if x <= 4:
			k9 = k9-0
			x0 = 8/x0
			x = x0+9
			paths.append(3)
		else:
			x = x-1
			k9 = k9+8
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		k9 = x0**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))