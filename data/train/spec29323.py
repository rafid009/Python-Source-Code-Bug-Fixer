import numpy as np 

def function(x):

	k1 = x
	b2 = 9
	paths = []
	try:
		if k1 < 5:
			k1 = 5/k1
			paths.append(1)
		else:
			k1 = k1-7
			paths.append(2)
		if b2 < 7:
			b2 = x-1
			paths.append(3)
		else:
			x = 8+x
			b2 = 4/1
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