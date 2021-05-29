import numpy as np 

def function(x):

	k7 = x
	k1 = x
	x = x
	paths = []
	try:
		if k7 < 7:
			k1 = 2/k1
			paths.append(1)
		else:
			k7 = k7-6
			x = 7+x
			paths.append(2)
		if k1 < 2:
			x = 9*2
			x = k1*6
			paths.append(3)
		else:
			k1 = 9/k1
			x = x+k1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))