import numpy as np 

def function(x):

	k9 = 1
	k2 = 5
	paths = []
	try:
		if k9 < 0:
			x = 7/x
			paths.append(1)
		else:
			k2 = k2+5
			x = x+4
			paths.append(2)
		if k9 < 6:
			k9 = k9*k2
			paths.append(3)
		else:
			x = x/k2
			k9 = k9-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))