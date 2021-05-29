import numpy as np 

def function(x):

	k1 = 1
	u5 = x
	paths = []
	try:
		if k1 > 4:
			k1 = k1+1
			paths.append(1)
		else:
			k1 = 7+u5
			paths.append(2)
		if x <= 9:
			x = k1-8
			paths.append(3)
		else:
			k1 = k1+u5
			k1 = 1/k1
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