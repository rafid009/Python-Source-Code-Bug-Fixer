import numpy as np 

def function(x):

	b3 = 7
	k1 = 0
	paths = []
	try:
		if x >= 6:
			x = 9+x
			paths.append(1)
		else:
			b3 = 4-8
			paths.append(2)
		if b3 > 3:
			k1 = k1-2
			b3 = b3+b3
			x = 1*3
			paths.append(3)
		else:
			k1 = k1+5
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