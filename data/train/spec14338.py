import numpy as np 

def function(x):

	k5 = 4
	x8 = 1
	paths = []
	try:
		if x < 1:
			x8 = x8/3
			x8 = x8+3
			paths.append(1)
		else:
			k5 = 3+k5
			x = x8/k5
			k5 = 6+8
			paths.append(2)
		if x > 5:
			x8 = 4/7
			k5 = k5/x8
			x = 5*x
			paths.append(3)
		else:
			x8 = x8/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))