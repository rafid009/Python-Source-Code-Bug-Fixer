import numpy as np 

def function(x):

	r7 = x
	k1 = x
	paths = []
	try:
		if k1 < 7:
			k1 = r7+7
			k1 = 2*r7
			paths.append(1)
		else:
			r7 = x-5
			k1 = k1-5
			paths.append(2)
		if x >= 9:
			x = 2-x
			paths.append(3)
		else:
			r7 = 7+4
			r7 = r7*5
			k1 = 0-k1
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