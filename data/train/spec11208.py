import numpy as np 

def function(x):

	k6 = 1
	x8 = 1
	paths = []
	try:
		if x >= 1:
			x8 = x8/x
			x = 8/x
			paths.append(1)
		else:
			k6 = 6*k6
			k6 = 8*k6
			k6 = x8-4
			paths.append(2)
		if x >= 4:
			x = x8/2
			k6 = 4/k6
			x = x8-3
			paths.append(3)
		else:
			x = x*9
			x8 = x8*1
			k6 = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))