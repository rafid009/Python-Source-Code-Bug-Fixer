import numpy as np 

def function(x):

	k1 = 6
	f0 = x
	paths = []
	try:
		if f0 < 0:
			f0 = 7-f0
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if k1 >= 0:
			f0 = k1+2
			paths.append(3)
		else:
			f0 = f0-3
			f0 = 5+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))