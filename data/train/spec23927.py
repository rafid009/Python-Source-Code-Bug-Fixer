import numpy as np 

def function(x):

	k1 = x
	v5 = x
	paths = []
	try:
		if k1 < 0:
			v5 = k1-1
			k1 = 3+k1
			paths.append(1)
		else:
			x = 8/x
			x = 1+7
			v5 = v5+5
			paths.append(2)
		if v5 > 3:
			k1 = k1+k1
			k1 = x-x
			x = x/2
			paths.append(3)
		else:
			x = x/9
			x = 6*x
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