import numpy as np 

def function(x):

	j9 = 0
	k1 = 2
	paths = []
	try:
		if k1 < 0:
			j9 = 5-j9
			x = k1+4
			k1 = k1+x
			paths.append(1)
		else:
			j9 = k1*j9
			j9 = j9+5
			paths.append(2)
		if k1 < 8:
			j9 = k1-j9
			j9 = j9/k1
			k1 = 1/k1
			paths.append(3)
		else:
			k1 = k1-k1
			k1 = k1*k1
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